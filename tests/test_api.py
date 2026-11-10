
from fastapi.testclient import TestClient

from app.main import app
from app.schemas import Finding


client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_extract_endpoint_returns_findings(monkeypatch):
    mock_findings = [
        Finding(
            sign_id="reduced_appetite",
            value="yes",
            quote="not eating properly"
        )
    ]

    monkeypatch.setattr(
        "app.main.extract_findings",
        lambda message: mock_findings
    )

    response = client.post(
        "/extract",
        json={
            "message": "The cow is not eating properly."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data["findings"]) == 1
    assert data["findings"][0]["sign_id"] == "reduced_appetite"
    assert data["escalate"] is False


def test_extract_endpoint_escalates_emergency_sign(monkeypatch):
    mock_findings = [
        Finding(
            sign_id="froth_nose_mouth",
            value="yes",
            quote="foam coming from its mouth"
        )
    ]

    monkeypatch.setattr(
        "app.main.extract_findings",
        lambda message: mock_findings
    )

    response = client.post(
        "/extract",
        json={
            "message": "There is foam coming from its mouth."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["escalate"] is True
    assert "froth_nose_mouth" in data["reason"]


def test_extract_endpoint_escalates_uncertain_emergency_sign(monkeypatch):
    mock_findings = [
        Finding(
            sign_id="cloudy_eye",
            value="not_sure",
            quote="maybe its eye is cloudy"
        )
    ]

    monkeypatch.setattr(
        "app.main.extract_findings",
        lambda message: mock_findings
    )

    response = client.post(
        "/extract",
        json={
            "message": "Maybe its eye is cloudy."
        }
    )

    assert response.status_code == 200
    assert response.json()["escalate"] is True


def test_extract_endpoint_rejects_empty_message():
    response = client.post(
        "/extract",
        json={"message": ""}
    )

    assert response.status_code == 422


def test_extract_endpoint_rejects_missing_message():
    response = client.post(
        "/extract",
        json={}
    )

    assert response.status_code == 422


def test_extract_endpoint_handles_provider_failure(monkeypatch):
    def failing_extractor(message):
        raise RuntimeError("Ollama is unavailable")

    monkeypatch.setattr(
        "app.main.extract_findings",
        failing_extractor
    )

    response = client.post(
        "/extract",
        json={"message": "The cow is not eating."}
    )

    assert response.status_code == 502
    assert "Ollama is unavailable" in response.json()["detail"]
