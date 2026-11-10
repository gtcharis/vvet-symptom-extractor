
from app.schemas import Finding
from app.escalation import determine_escalation


def make_finding(sign_id, value, quote="test evidence"):
    return Finding(
        sign_id=sign_id,
        value=value,
        quote=quote
    )


def test_froth_triggers_escalation():
    findings = [
        make_finding("froth_nose_mouth", "yes")
    ]

    escalate, reason = determine_escalation(findings)

    assert escalate is True
    assert "froth_nose_mouth" in reason


def test_unable_to_stand_triggers_escalation():
    findings = [
        make_finding("unable_to_stand", "yes")
    ]

    escalate, reason = determine_escalation(findings)

    assert escalate is True
    assert "unable_to_stand" in reason


def test_cloudy_eye_triggers_escalation():
    findings = [
        make_finding("cloudy_eye", "yes")
    ]

    escalate, reason = determine_escalation(findings)

    assert escalate is True
    assert "cloudy_eye" in reason


def test_uncertain_emergency_sign_triggers_escalation():
    findings = [
        make_finding("cloudy_eye", "not_sure")
    ]

    escalate, reason = determine_escalation(findings)

    assert escalate is True
    assert "cloudy_eye" in reason


def test_no_escalation_for_non_emergency_signs():
    findings = [
        make_finding("reduced_appetite", "yes"),
        make_finding("swelling", "yes"),
        make_finding("ticks", "yes")
    ]

    escalate, reason = determine_escalation(findings)

    assert escalate is False


def test_explicitly_denied_emergency_sign_does_not_escalate():
    findings = [
        make_finding("froth_nose_mouth", "no"),
        make_finding("cloudy_eye", "no")
    ]

    escalate, reason = determine_escalation(findings)

    assert escalate is False


def test_empty_findings_do_not_escalate():
    escalate, reason = determine_escalation([])

    assert escalate is False
    assert "No escalation" in reason
