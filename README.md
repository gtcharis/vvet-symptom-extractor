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
| Language model | Qwen 2.5 3B |
| HTTP client | HTTPX |
| Testing | Pytest |
| API testing | FastAPI TestClient |
| Model response format | JSON schema-constrained output |

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

Each finding is classified as:

- `yes`: The farmer reports the sign.
- `no`: The farmer explicitly denies the sign or describes its absence.
- `not_sure`: The farmer expresses uncertainty about the sign.

Signs that are not mentioned are omitted rather than automatically classified as absent.

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
Ollama / Qwen 2.5 3B
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

### Design Decisions

#### LLM-based extraction

The LLM interprets natural-language messages and identifies relevant health signs. This supports informal descriptions and expressions that may not be captured reliably by simple keyword matching.

The extraction prompt provides the model with the approved health-sign vocabulary and instructions for interpreting reported, denied, and uncertain observations.

The implementation includes guidance for English, Shona, isiNdebele, and code-switching.

#### Controlled vocabulary

The extractor receives a fixed list of approved sign IDs and their descriptions. This limits the output to the assessment's required vocabulary.

Pydantic schemas provide an additional validation layer to reject unsupported identifiers and invalid classification values.

#### Evidence-based findings

Every finding must include a quotation from the farmer's original message.

The application checks that the normalized quotation appears in the original message before accepting the finding. This helps prevent the model from returning unsupported or paraphrased evidence.

#### Deterministic escalation

Escalation is handled by ordinary application code rather than delegated to the LLM.

This makes the critical decision rules explicit, testable, and predictable.

## 5. Escalation Rules

The system escalates when any of the following signs is reported as `yes` or `not_sure`:

- `froth_nose_mouth`
- `unable_to_stand`
- `cloudy_eye`

A sign classified as `no` does not trigger escalation.

The escalation engine operates independently of the language model.

This separation ensures that the model is responsible for interpreting the farmer's message, while Python enforces the predefined escalation criteria.

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
│   ├── evaluation.py
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
│   ├── evaluation_cases.py
│   ├── validation_cases.py
│   └── test_cases.py
│
├── scripts/
│   └── run_evaluation.py
│
├── evaluation_results/
│   ├── training_results.json
│   ├── validation_results.json
│   └── test_results.json
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
git clone https://github.com/gtcharis/vvet-symptom-extractor.git
cd vvet-symptom-extractor
```

### Create a virtual environment

Windows PowerShell:

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

The `.env` file is excluded from version control. A `.env.example` file is provided as a configuration reference.

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
python -m pytest -v
```

The test suite uses mocked LLM responses where appropriate, allowing tests to run without downloading a model, requiring an API key, or making external LLM requests.

## 11. Evaluation Methodology

The model was evaluated using three manually labelled datasets:

| Dataset | Purpose | Cases |
|---|---|---:|
| Training | Development and prompt evaluation | 65 |
| Validation | Assessing generalisation | 50 |
| Test | Final held-out evaluation | 50 |
| **Total** | | **165** |

The datasets contain examples covering:

- All nine approved health signs.
- Explicitly denied symptoms.
- Uncertain symptom descriptions.
- Multiple symptoms in one message.
- English and local-language expressions, including Shona and isiNdebele.

The evaluation script compares model predictions against expected sign/value pairs and calculates:

- Precision.
- Recall.
- F1 score.
- Exact case matches.
- Failed inference runs.

A wrong classification value is counted as both a false positive and a false negative.

### Evaluation Results

| Metric | Training | Validation | Test |
|---|---:|---:|---:|
| Total cases | 65 | 50 | 50 |
| Successful runs | 63 | 44 | 46 |
| Failed runs | 2 | 6 | 4 |
| Exact matches | 54 | 24 | 27 |
| Exact match rate | 83.08% | 48.00% | 54.00% |
| Precision | 92.94% | 65.45% | 74.07% |
| Recall | 89.77% | 63.16% | 66.67% |
| F1 score | 91.33% | 64.29% | 70.18% |

The final test dataset produced:

- **Precision:** 74.07%
- **Recall:** 66.67%
- **F1 score:** 70.18%
- **Exact match rate:** 54.00%
- **Successful inference runs:** 46 out of 50
- **Failed inference runs:** 4 out of 50

Precision, recall, and F1 are calculated over successful extraction runs, while failed runs are reported separately. Exact-match rate uses the total number of dataset cases.

### Interpretation

The model achieved an F1 score of 91.33% on the development dataset, 64.29% on validation, and 70.18% on the final test dataset.

The difference between development and held-out performance indicates a generalisation gap.

The validation and test results show that the model does not interpret all natural-language descriptions consistently. Observed challenges include:

- Some Shona and isiNdebele symptom descriptions.
- Uncertainty being classified as a definite positive.
- Messages containing multiple health signs.
- Distinguishing weakness from inability to stand.
- Evidence quotations that paraphrase rather than reproduce the original wording.
- Inference failures caused by invalid evidence quotations.

The evaluation datasets are manually constructed examples rather than a large, statistically representative collection of real farmer reports. The results should therefore be treated as preliminary indicators of extraction performance, not evidence of clinical accuracy.

## 12. Development and Evaluation Environment

The project was developed and evaluated on the following environment:

| Component | Specification |
|---|---|
| Operating System | Windows |
| Processor | Intel Core i7-1165G7, 11th Generation |
| Memory | 8 GB RAM |
| Graphics | Intel Integrated Graphics |
| Python | 3.15.2 |
| API Framework | FastAPI |
| LLM Runtime | Ollama 0.40.16 |
| Language Model | Qwen 2.5 3B |
| Testing Framework | Pytest |
| API Testing | FastAPI TestClient / HTTPX |

### Model Configuration

| Configuration | Value |
|---|---|
| Model | `qwen2.5:3b` |
| Runtime | Ollama |
| Temperature | `0` |
| Context window | `2048` tokens |
| Response format | JSON schema-constrained output |
| Streaming | Disabled |
| Inference | Local |

### Configuration Rationale

- **Local inference:** Allows the application to run without depending on an external LLM API.
- **Temperature 0:** Encourages consistent, less variable extraction responses.
- **JSON schema:** Constrains the model's response to the expected structured output.
- **Context window 2048:** Keeps the inference configuration modest for the available hardware.

Evaluation runs were performed sequentially to minimise resource contention during local model inference.

## 13. Limitations and Future Improvements

Potential improvements include:

1. Expanding the evaluation dataset with reviewed, real-world farmer messages.
2. Supporting more Zimbabwean local-language expressions and spelling variations.
3. Evaluating additional LLMs for extraction accuracy and inference speed.
4. Improving confidence handling and ambiguous symptom detection.
5. Investigating evidence quotation and duplicate-finding failures.
6. Introducing structured logging and monitoring.
7. Adding authentication and rate limiting for production use.
8. Building a human-review workflow for uncertain findings.
9. Measuring sign-level detection performance separately from classification-value accuracy.
10. Validating the extraction and escalation workflow with veterinary professionals.

## 14. AI Development Assistance

AI coding assistance was used during development to support implementation, debugging, test design, and documentation.

The architecture, implementation decisions, validation approach, and testing process were reviewed and executed as part of the development work.

## 15. Safety Considerations

This project is a symptom extraction and triage-support prototype. It is not a veterinary diagnostic system.

An escalation decision indicates that one or more predefined signs warrant veterinary attention. It does not establish a diagnosis or replace professional assessment.

The model may miss, misinterpret, or incorrectly classify reported signs. The evaluation results demonstrate these limitations. Any real-world deployment should include veterinary oversight, human review, and further validation using representative farmer reports.

---

**Project:** V-Vet Livestock Symptom Extraction API  
**Author:** Godfrey Charis  
**Language:** Python  
**API Framework:** FastAPI  
**LLM Runtime:** Ollama  
**Model:** Qwen 2.5 3B  
**Repository:** https://github.com/gtcharis/vvet-symptom-extractor