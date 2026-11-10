
import json
import sys
from pathlib import Path

# Ensure the project root is available for imports.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.extractor import extract_findings
from app.evaluation import calculate_metrics
from tests.evaluation_cases import EVALUATION_CASES


def run_evaluation():
    results = []
    successful_expected = []
    successful_actual = []

    print("\nV-Vet Model Evaluation")
    print("=" * 50)

    for case in EVALUATION_CASES:
        case_id = case["id"]

        print(f"\nRunning {case_id}...")

        try:
            findings = extract_findings(case["message"])

            actual = {
                finding.sign_id: finding.value
                for finding in findings
            }

            expected = case["expected"]

            successful_expected.append(expected)
            successful_actual.append(actual)

            matched = expected == actual

            result = {
                "id": case_id,
                "message": case["message"],
                "expected": expected,
                "actual": actual,
                "passed": matched,
                "error": None
            }

            print("PASS" if matched else "MISMATCH")

        except Exception as exc:
            result = {
                "id": case_id,
                "message": case["message"],
                "expected": case["expected"],
                "actual": None,
                "passed": False,
                "error": str(exc)
            }

            print(f"ERROR: {exc}")

        results.append(result)

    metrics = calculate_metrics(
        successful_expected,
        successful_actual
    )

    successful_count = len(successful_expected)
    failed_count = len(results) - successful_count

    summary = {
        "total_cases": len(EVALUATION_CASES),
        "successful_runs": successful_count,
        "failed_runs": failed_count,
        "exact_matches": sum(
            1 for result in results if result["passed"]
        ),
        "metrics": metrics
    }

    report = {
        "summary": summary,
        "results": results
    }

    output_path = PROJECT_ROOT / "evaluation_results.json"

    output_path.write_text(
        json.dumps(report, indent=4, ensure_ascii=False),
        encoding="utf-8"
    )

    print("\n" + "=" * 50)
    print("EVALUATION SUMMARY")
    print("=" * 50)

    print(f"Total cases:       {summary['total_cases']}")
    print(f"Successful runs:   {successful_count}")
    print(f"Failed runs:       {failed_count}")
    print(f"Exact matches:     {summary['exact_matches']}")
    print(f"Precision:         {metrics['precision']:.2%}")
    print(f"Recall:            {metrics['recall']:.2%}")
    print(f"F1 score:          {metrics['f1']:.2%}")

    print(f"\nFull report saved to: {output_path}")


if __name__ == "__main__":
    run_evaluation()
