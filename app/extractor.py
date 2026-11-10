
from pydantic import ValidationError

from app.llm.provider import generate_json
from app.schemas import Finding
from app.signs import SIGNS


def build_extraction_prompt(message: str) -> str:
    sign_descriptions = "\n".join(
        f"- {sign_id}: {description}"
        for sign_id, description in SIGNS.items()
    )

    return f"""
You are a livestock health symptom extraction assistant.

Your task is to identify which of the approved signs are mentioned
in the farmer's message.

APPROVED SIGNS:
{sign_descriptions}

RULES:
1. Only use the approved sign IDs listed above.
2. Only report signs supported by the farmer's actual message.
3. Do not diagnose diseases or infer symptoms that were not mentioned.
4. Use "yes" when the farmer clearly reports a sign.
5. Use "no" when the farmer explicitly denies a sign.
6. Use "not_sure" when the farmer expresses uncertainty about a sign.
7. Do not report a sign simply because it was not mentioned.
8. Include a short, exact quotation from the farmer's message
   as evidence for every finding.
9. Preserve the farmer's original wording, including Shona-English
   expressions where possible.
10. Return each sign at most once.

OUTPUT:
Return valid JSON only, using exactly this structure:

{{
    "findings": [
        {{
            "sign_id": "reduced_appetite",
            "value": "yes",
            "quote": "The animal has stopped eating"
        }}
    ]
}}

If no approved signs are mentioned, return:

{{
    "findings": []
}}

FARMER'S MESSAGE:
{message}
"""


def normalize_text(text: str) -> str:
    """Normalize whitespace and casing for evidence comparison."""
    return " ".join(text.casefold().split())


def extract_findings(message: str) -> list[Finding]:
    """
    Extract and validate livestock health findings
    using the configured LLM provider.
    """

    prompt = build_extraction_prompt(message)

    result = generate_json(prompt)

    if not isinstance(result, dict):
        raise ValueError("LLM response must be a JSON object.")

    raw_findings = result.get("findings")

    if not isinstance(raw_findings, list):
        raise ValueError("LLM response must contain a findings list.")

    validated_findings = []
    seen_signs = set()

    for raw_finding in raw_findings:

        # Validate approved sign ID, value and quote.
        try:
            finding = Finding.model_validate(raw_finding)
        except ValidationError as exc:
            raise ValueError(
                f"LLM returned an invalid finding: {exc}"
            ) from exc

        # Ensure every evidence quote actually appears
        # in the original farmer message.
        quote = normalize_text(finding.quote)
        original_message = normalize_text(message)

        if not quote or quote not in original_message:
            raise ValueError(
                f"Evidence quote is not present in the message: "
                f"{finding.quote}"
            )

        # Prevent duplicate findings for the same sign.
        if finding.sign_id in seen_signs:
            continue

        seen_signs.add(finding.sign_id)
        validated_findings.append(finding)

    return validated_findings
