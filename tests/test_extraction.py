
import pytest

from app.extractor import extract_findings


def test_extracts_valid_findings(monkeypatch):
    mock_response = {
        "findings": [
            {
                "sign_id": "reduced_appetite",
                "value": "yes",
                "quote": "not eating properly"
            }
        ]
    }

    monkeypatch.setattr(
        "app.extractor.generate_json",
        lambda prompt: mock_response
    )

    findings = extract_findings("The cow is not eating properly.")

    assert len(findings) == 1
    assert findings[0].sign_id == "reduced_appetite"
    assert findings[0].value == "yes"


def test_rejects_unknown_sign_id(monkeypatch):
    mock_response = {
        "findings": [
            {
                "sign_id": "fever",
                "value": "yes",
                "quote": "has a fever"
            }
        ]
    }

    monkeypatch.setattr(
        "app.extractor.generate_json",
        lambda prompt: mock_response
    )

    with pytest.raises(ValueError, match="invalid finding"):
        extract_findings("The cow has a fever.")


def test_rejects_invalid_value(monkeypatch):
    mock_response = {
        "findings": [
            {
                "sign_id": "ticks",
                "value": "maybe",
                "quote": "there are ticks"
            }
        ]
    }

    monkeypatch.setattr(
        "app.extractor.generate_json",
        lambda prompt: mock_response
    )

    with pytest.raises(ValueError, match="invalid finding"):
        extract_findings("There are ticks on the cow.")


def test_rejects_quote_not_in_original_message(monkeypatch):
    mock_response = {
        "findings": [
            {
                "sign_id": "ticks",
                "value": "yes",
                "quote": "The animal has many ticks"
            }
        ]
    }

    monkeypatch.setattr(
        "app.extractor.generate_json",
        lambda prompt: mock_response
    )

    with pytest.raises(ValueError, match="Evidence quote"):
        extract_findings("I noticed something unusual on the cow.")


def test_returns_empty_list_when_no_signs_found(monkeypatch):
    monkeypatch.setattr(
        "app.extractor.generate_json",
        lambda prompt: {"findings": []}
    )

    findings = extract_findings("The cow is behaving normally.")

    assert findings == []


def test_prevents_duplicate_signs(monkeypatch):
    mock_response = {
        "findings": [
            {
                "sign_id": "ticks",
                "value": "yes",
                "quote": "ticks on the legs"
            },
            {
                "sign_id": "ticks",
                "value": "yes",
                "quote": "ticks on the body"
            }
        ]
    }

    monkeypatch.setattr(
        "app.extractor.generate_json",
        lambda prompt: mock_response
    )

    findings = extract_findings(
        "There are ticks on the legs and ticks on the body."
    )

    assert len(findings) == 1
    assert findings[0].sign_id == "ticks"


def test_rejects_missing_findings_field(monkeypatch):
    monkeypatch.setattr(
        "app.extractor.generate_json",
        lambda prompt: {}
    )

    with pytest.raises(ValueError, match="findings list"):
        extract_findings("The cow is not eating.")


def test_provider_prompt_contains_all_approved_signs(monkeypatch):
    captured = {}

    def mock_generate(prompt):
        captured["prompt"] = prompt
        return {"findings": []}

    monkeypatch.setattr(
        "app.extractor.generate_json",
        mock_generate
    )

    extract_findings("The animal seems fine.")

    for sign_id in [
        "reduced_appetite",
        "weakness",
        "swelling",
        "rapid_breathing",
        "cloudy_eye",
        "froth_nose_mouth",
        "red_urine",
        "unable_to_stand",
        "ticks"
    ]:
        assert sign_id in captured["prompt"]
