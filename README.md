# V-Vet Livestock Symptom Extraction API

A Python-based API that extracts structured livestock health signs from farmer messages using a Large Language Model (LLM), validates the extracted information, and determines whether veterinary escalation is required.

## 1. Project Overview

Farmers often describe animal health problems using informal language, local expressions, and a mixture of languages. This project converts those descriptions into structured symptom data that can support veterinary triage.

The API accepts a farmer's message and returns:

- Identified livestock health signs.
- A classification for each sign: `yes`, `no`, or `not_sure`.
- A supporting quotation from the original message.
- An escalation decision.
- A reason explaining the escalation decision.

The system extracts symptoms; it does not diagnose diseases or prescribe treatment.

## 2. Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| API framework | FastAPI |
| Data validation | Pydantic |
| LLM runtime | Ollama |
| Language model | Qwen2.5 3B |
| HTTP client | HTTPX |
| Testing | Pytest |
| API testing | FastAPI TestClient |

The language model runs locally through Ollama, avoiding dependence on a paid external LLM API.

## 3. Approved Health Signs

The extractor is restricted to nine approved livestock health signs:

| Sign ID | Description |
|---|---|
| `reduced_appetite` | Eating less than usual or stopped eating/grazing |
| `weakness` | Dull, weak, or lying down more than usual |
| `swelling` | Lump below the ear, under the jaw, or in front of the shoulder; may be called mbandabvu |
| `rapid_breathing` | Breathing unusually fast while resting |
| `cloudy_eye` | Eye appearing white, grey, or milky |
| `froth_nose_mouth` | Foam or froth coming from the nose or mouth |
| `red_urine` | Red, brown, or strong tea-coloured urine |
| `unable_to_stand` | Unable to get up or remain standing |
| `ticks` | Ticks visible on the animal |

Only approved sign IDs are accepted in the API response.

## 4. System Architecture

The application separates language understanding, data validation, and escalation logic.

```text
Farmer Message
      |
      v
POST /extract
      |
      v
Extraction Service
      |
      v
Prompt Construction
      |
      v
Ollama / Qwen2.5 3B
      |
      v
Structured JSON Response
      |
      v
Pydantic Validation
      |
      v
Evidence Quote Validation
      |
      v
Escalation Rules Engine
      |
      v
Structured API Response
```

### Design decisions

**LLM-based extraction**

The LLM interprets natural-language messages and identifies relevant health signs. This supports informal descriptions and expressions that may not be captured reliably by simple keyword matching.

**Controlled vocabulary**

The extractor receives a fixed list of approved sign IDs and their descriptions. This limits the output to the assessment's required vocabulary.

**Evidence-based findings**

Every finding must include a quotation from the farmer's original message. The application checks that the quotation appears in the original message before accepting the finding.

**Deterministic escalation**

Escalation is handled by ordinary application code rather than delegated to the LLM. This makes the critical decision rules explicit, testable, and predictable.

## 5. Escalation Rules

The system escalates when any of the following signs is reported as `yes` or `not_sure`:

- `froth_nose_mouth`
- `unable_to_stand`
- `cloudy_eye`

A sign classified as `no` does not trigger escalation.

The escalation engine operates independently of the language model.

## 6. Project Structure

```text
vvet-symptom-extractor/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── signs.py
│   ├── extractor.py
│   ├── escalation.py
│   │
│   └── llm/
│       ├── __init__.py
│       └── provider.py
│
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_extraction.py
│   ├── test_escalation.py
│   ├── test_evaluation.py
│   └── evaluation_cases.py
│
├── scripts/
│   └── run_evaluation.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 7. Setup and Installation

### Prerequisites

- Python 3.10 or later.
- Ollama installed.
- Git.

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/vvet-symptom-extractor.git
cd vvet-symptom-extractor
```

### Create a virtual environment

Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root:

```env
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=qwen2.5:3b
```

### Download the model

```bash
ollama pull qwen2.5:3b
```

Ensure Ollama is running before starting the API.

## 8. Running the Application

Start the API:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Health check:

```http
GET /
```

## 9. API Usage

### Endpoint

```http
POST /extract
Content-Type: application/json
```

### Request

```json
{
  "message": "The cow has stopped eating and foam is coming out of its mouth."
}
```

### Example response

```json
{
  "findings": [
    {
      "sign_id": "reduced_appetite",
      "value": "yes",
      "quote": "The cow has stopped eating"
    },
    {
      "sign_id": "froth_nose_mouth",
      "value": "yes",
      "quote": "foam is coming out of its mouth"
    }
  ],
  "escalate": true,
  "reason": "Escalation required due to: froth_nose_mouth"
}
```

The example illustrates the expected response structure. Actual extraction results depend on the language model's interpretation of the input.

## 10. Testing

The project includes automated tests for:

- API endpoint behaviour.
- Request validation.
- Approved sign ID validation.
- Invalid classification rejection.
- Evidence quotation validation.
- Duplicate finding handling.
- Escalation rules.
- Uncertain emergency findings.
- Evaluation metric calculations.
- LLM provider failure handling.

Run the test suite:

```bash
pytest -v
```

The test suite uses mocked LLM responses where appropriate, allowing tests to run without downloading a model, requiring an API key, or making external LLM requests.

## 11. Evaluation Methodology

A small, manually labelled evaluation dataset is maintained in `tests/evaluation_cases.py`.

It contains examples covering:

- All nine approved health signs.
- Explicitly denied symptoms.
- Uncertain symptom descriptions.
- Multiple symptoms in one message.
- English and Shona-English expressions.

The evaluation script compares model predictions against expected sign/value pairs and calculates:

- Precision.
- Recall.
- F1 score.
- Exact case matches.
- Failed inference runs.

A wrong classification value is counted as both a false positive and a false negative.

The current evaluation examples are development cases, not an official V-Vet dataset or a statistically representative sample. Reported metrics should therefore be interpreted as preliminary indicators rather than evidence of clinical accuracy.

## 12. Limitations and Future Improvements

Potential improvements include:

1. Expanding the evaluation dataset with reviewed, real-world farmer messages.
2. Supporting more Zimbabwean local-language expressions and spelling variations.
3. Evaluating additional LLMs for extraction accuracy and inference speed.
4. Improving confidence handling and ambiguous symptom detection.
5. Introducing structured logging and monitoring.
6. Adding authentication and rate limiting for production use.
7. Building a human-review workflow for uncertain findings.
8. Measuring sign-level detection performance separately from classification-value accuracy.

## 13. AI Development Assistance

AI coding assistance was used during development to support implementation, debugging, test design, and documentation. The architecture, implementation decisions, validation approach, and testing process were reviewed and executed as part of the development work.

---

**Project:** V-Vet Livestock Symptom Extraction API  
**Author:** Godfrey Charis  
**Language:** Python  
**API Framework:** FastAPI  
**LLM Runtime:** Ollama
