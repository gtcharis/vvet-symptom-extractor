
from pydantic import ValidationError

from app.llm.provider import generate_json
from app.schemas import Finding, ExtractionResult
from app.signs import SIGNS


def build_extraction_prompt(message: str) -> str:
    sign_descriptions = "\n".join(
        f"- {sign_id}: {description}"
        for sign_id, description in SIGNS.items()
    )

    return f"""
You are a precise multilingual livestock health information
extraction system for farmers in Zimbabwe.

TASK:
Identify the approved livestock health signs explicitly
reported, denied or expressed uncertainly in the message.

SUPPORTED LANGUAGES:
- English
- Shona
- isiNdebele
- Shona-English code-switching
- Ndebele-English code-switching

APPROVED SIGNS:
{sign_descriptions}

LANGUAGE UNDERSTANDING:

Understand informal expressions, colloquial language,
common spelling variations and mixed-language sentences.

SHONA EXAMPLES:

- "kudya zvishoma" = eating less
- "haichadyi" = no longer eating
- "haina simba" = has no strength / is weak
- "ine zvikwekwe" = has ticks
- "haina zvikwekwe" = has no ticks
- "inokwanisa kusimuka" = can get up
- "haikwanisi kusimuka" = cannot get up

ISINDEBELE EXAMPLES:

- "ayidli kahle" = is not eating well
- "ayisadli" = no longer eating
- "ayilamandla" = has no strength / is weak
- "ilemikhaza" = has ticks
- "ayinalo imikhaza" = has no ticks
- "iyenelisa ukusukuma" = can get up
- "ayehluleka ukusukuma" = cannot get up

Interpret these expressions in their full sentence context.

IMPORTANT DISTINCTION:

Weakness and inability to stand are separate signs.

For example:

"Ayilamandla kodwa iyenelisa ukusukuma."

Must produce:
- weakness = yes
- unable_to_stand = no

Do not interpret weakness as inability to stand.

IMPORTANT CODE-SWITCHING RULE:

A single message may contain multiple signs expressed
in different languages.

Extract ALL identifiable signs independently.

Do not stop extracting after identifying one sign.

For example:

"The cow haina simba and cannot get up."

Must produce:
- weakness = yes, quote = "haina simba"
- unable_to_stand = yes, quote = "cannot get up"

"The cow is eating normally but ine zvikwekwe."

Must produce:
- reduced_appetite = no
- ticks = yes

Do not allow an English expression to overshadow
a Shona or isiNdebele expression in the same message.

CLASSIFICATION:
- yes: The farmer clearly reports the sign.
- no: The farmer explicitly denies the sign.
- not_sure: The farmer expresses uncertainty about the sign.
- Do not omit explicitly denied signs.
- Do not report signs that are neither reported nor denied.
- Do not infer symptoms or diagnose diseases.
- Return each sign at most once.

EXAMPLES OF CLASSIFICATION:
1. "The cow has no swelling."
   -> swelling = no

2. "The cow is eating normally."
   -> reduced_appetite = no

3. "I haven't noticed any ticks."
   -> ticks = no

4. "Maybe the cow's eye is cloudy."
   -> cloudy_eye = not_sure

5. "Mombe iri kudya zvishoma."
   -> reduced_appetite = yes

6. "The cow ine zvikwekwe."
   -> ticks = yes

STRICT SIGN INDEPENDENCE:

Each approved sign must be evaluated independently.

A statement about one sign must never be used as evidence
for another sign.

Examples:

1. "The cow is weak and lying down."
   -> weakness = yes
   -> Do NOT infer unable_to_stand.

2. "The cow has no ticks."
   -> ticks = no
   -> Do NOT create findings for other signs.

3. "The cow is fine, but has many ticks."
   -> ticks = yes
   -> Do NOT infer that any other sign is absent.

4. "The cow is not breathing fast, has no swelling,
   and has no ticks."
   -> rapid_breathing = no
   -> swelling = no
   -> ticks = no
   -> Do NOT create weakness = no.

5. "The cow can stand and walk normally."
   -> unable_to_stand = no

A general statement such as "the animal is fine",
"the animal looks healthy", or "the calf is okay"
does not establish the presence or absence of any
individual approved sign.

Only return negative findings when the message provides
specific evidence that the particular sign is absent.

NORMAL OBSERVATIONS AND NEGATIVE FINDINGS:

A normal observation can establish that the corresponding
abnormal sign is absent.

Examples:

- "The cow is eating normally."
  -> reduced_appetite = no

- "Its appetite seems fine."
  -> reduced_appetite = no

- "It breathes normally while resting."
  -> rapid_breathing = no

- "It is not breathing fast at rest."
  -> rapid_breathing = no

- "There is no foam around its mouth."
  -> froth_nose_mouth = no

- "The cow can get up and stand normally."
  -> unable_to_stand = no

- "There is no swelling under the jaw."
  -> swelling = no

Do not omit an explicitly stated normal observation
simply because another sign is also reported.

For example:

"The cow has ticks, but is eating normally."

Must produce:
- ticks = yes
- reduced_appetite = no

EVIDENCE RULES:

- Every finding must contain evidence copied directly from
  the farmer's original message.
- The quote must be a continuous substring of that message.
- Preserve the original spelling, casing and language.
- Never translate, paraphrase, rewrite or correct a quote.
- The approved sign descriptions are reference material,
  NOT evidence.
- Never copy wording from sign descriptions or examples
  into a quote unless those exact words appear in the message.
- For negative findings, quote the words expressing absence.
- For uncertain findings, quote the words expressing doubt.
- Prefer the shortest meaningful phrase that supports the finding.
- If no valid supporting quote can be identified, do not
  fabricate evidence.

Before returning the response, verify every quote against
the farmer's original message.

UNCERTAINTY SCOPE:

Apply uncertainty only to the specific sign or observation
that the farmer expresses doubt about.

Examples:

1. "Maybe the cow is eating less."
   -> reduced_appetite = not_sure

2. "It may be weak."
   -> weakness = not_sure

3. "I'm unsure whether it can stand."
   -> unable_to_stand = not_sure

4. "I don't know if there is swelling, but it is breathing
   very fast while resting."
   -> swelling = not_sure
   -> rapid_breathing = yes

5. "Maybe the cow is eating less, but I am certain
   there are ticks."
   -> reduced_appetite = not_sure
   -> ticks = yes

Do not classify an uncertain observation as yes merely
because it resembles an approved sign.

Do not omit an observation simply because the farmer
expresses uncertainty about it.

Do not transfer uncertainty between different signs.


FINAL SELF-CHECK:

Before returning JSON, verify:

1. Every finding corresponds to one of the nine approved signs.
2. Every finding is independently supported by the message.
3. No sign has been inferred from an unrelated observation.
4. Explicitly stated normal observations and negatives
   have been included.
5. Uncertain observations are classified as not_sure.
6. Weakness has not been confused with inability to stand.
7. Each sign appears only once.
8. Every evidence quote is copied from the original message.
9. Every quote is a continuous substring of the original
   farmer message.

If the same sign appears more than once, combine the evidence
and return one classification that reflects the complete
context. Never return conflicting values for one sign.

{{
  "findings": [
    {{
      "sign_id": "approved_sign_id",
      "value": "yes",
      "quote": "exact words copied from the message"
    }}
  ]
}}

If no approved signs are reported, denied or uncertain,
return:
{{"findings": []}}

FARMER'S ORIGINAL MESSAGE:
{message}
"""


def normalize_text(text: str) -> str:
    """
    Normalize text for evidence comparison.

    Converts text to lowercase using casefold() and collapses
    consecutive whitespace characters into single spaces.

    This allows evidence validation to tolerate differences
    in casing and whitespace while still requiring the quoted
    evidence to appear in the original farmer message.

    Note: This is normalized substring validation, not strict
    character-for-character verification.
    """
    return " ".join(text.casefold().split())


def extract_findings(message: str) -> list[Finding]:
    """
    Extract and validate livestock health findings.

    Validation includes:
    - Pydantic schema validation
    - Approved sign IDs and classification values
    - Normalized evidence substring verification
    - Duplicate sign detection
    - Rejection of conflicting duplicate classifications
    """

    prompt = build_extraction_prompt(message)

    # Request output constrained by the Pydantic JSON Schema.
    result = generate_json(
        prompt,
        schema=ExtractionResult.model_json_schema()
    )

    # Validate the complete response structure.
    try:
        extraction = ExtractionResult.model_validate(result)
    except ValidationError as exc:
        raise ValueError(
            f"LLM returned invalid extraction data: {exc}"
        ) from exc

    validated_findings = []
    seen_signs = {}

    # Normalize the original message once for evidence checks.
    original_message = normalize_text(message)

    for finding in extraction.findings:

        # Verify that evidence exists in the original message
        # after normalizing casing and whitespace.
        quote = normalize_text(finding.quote)

        if not quote or quote not in original_message:
            raise ValueError(
                f"Evidence quote is not present in the message: "
                f"{finding.quote}"
            )

        # Check whether this sign has already been extracted.
        if finding.sign_id in seen_signs:
            previous_finding = seen_signs[finding.sign_id]

            # Reject contradictory classifications.
            if previous_finding.value != finding.value:
                raise ValueError(
                    f"Conflicting duplicate findings for "
                    f"'{finding.sign_id}': "
                    f"'{previous_finding.value}' versus "
                    f"'{finding.value}'."
                )

            # Identical classifications are also duplicates.
            # Keep the first valid finding.
            continue

        seen_signs[finding.sign_id] = finding
        validated_findings.append(finding)

    return validated_findings
