
from fastapi import FastAPI, HTTPException

from app.schemas import ExtractRequest, ExtractResponse
from app.extractor import extract_findings
from app.escalation import determine_escalation


app = FastAPI(
    title="V-Vet Symptom Extraction API",
    description="Extract structured livestock health signs from farmer messages.",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "V-Vet Symptom Extraction API"
    }


@app.post("/extract", response_model=ExtractResponse)
def extract_symptoms(request: ExtractRequest):

    try:
        # Step 1: Extract and validate findings using the LLM.
        findings = extract_findings(request.message)

        # Step 2: Apply deterministic escalation rules.
        escalate, reason = determine_escalation(findings)

        # Step 3: Return the structured response.
        return ExtractResponse(
            findings=findings,
            escalate=escalate,
            reason=reason
        )

    except (RuntimeError, ValueError) as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Symptom extraction failed: {exc}"
        ) from exc
