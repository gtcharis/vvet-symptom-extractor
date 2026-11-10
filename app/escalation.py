ESCALATION_SIGNS = {
    "froth_nose_mouth",
    "unable_to_stand",
    "cloudy_eye"
}


def determine_escalation(findings):

    triggered_signs = [
        finding.sign_id
        for finding in findings
        if (
            finding.sign_id in ESCALATION_SIGNS
            and finding.value in {"yes", "not_sure"}
        )
    ]

    if triggered_signs:
        return (
            True,
            "Escalation required due to: "
            + ", ".join(triggered_signs)
        )

    return (
        False,
        "No escalation-triggering signs identified."
    )