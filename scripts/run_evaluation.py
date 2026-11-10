
import argparse
import json
import sys
from pathlib import Path

# Ensure the project root is available for imports.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app.extractor import extract_findings
from app.evaluation import calculate_metrics

# Dataset registry.
DATASETS = {
    "training": {
        "module": "tests.evaluation_cases",
        "variable": "EVALUATION_CASES",
    },
    "validation": {
        "module": "tests.validation_cases",
        "variable": "VALIDATION_CASES",
    },
    "test": {
        "module": "tests.test_cases",
        "variable": "TEST_CASES",
    },
}


def load_dataset(dataset_name):
    """Load the selected evaluation dataset."""

    from importlib import import_module

    config = DATASETS[dataset_name]
    module = import_module(config["module"])

    return getattr(module, config["variable"])


def run_evaluation(dataset_name):
    cases = load_dataset(dataset_name)

    results = []
    successful_expected = []
    successful_actual = []

    print(f"\nV-Vet Model Evaluation: {dataset_name.upper()}")
    print("=" * 55)

    for case in cases:
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
                "error": None,
            }

            print("PASS" if matched else "MISMATCH")

        except Exception as exc:
            result = {
                "id": case_id,
                "message": case["message"],
                "expected": case["expected"],
                "actual": None,
                "passed": False,
                "error": str(exc),
            }

            print(f"ERROR: {exc}")

        results.append(result)

    # Calculate metrics using successful extraction runs.
    if successful_expected:
        metrics = calculate_metrics(
            successful_expected,
            successful_actual,
        )
    else:
        metrics = {
            "precision": 0,
            "recall": 0,
            "f1": 0,
        }

    successful_count = len(successful_expected)
    failed_count = len(results) - successful_count
    exact_matches = sum(
        1 for result in results if result["passed"]
    )

    summary = {
        "dataset": dataset_name,
        "total_cases": len(cases),
        "successful_runs": successful_count,
        "failed_runs": failed_count,
        "exact_matches": exact_matches,
        "exact_match_rate": (
            exact_matches / len(cases) if cases else 0
        ),
        "metrics": metrics,
    }

    report = {
        "summary": summary,
        "results": results,
    }

    # Save each dataset's report separately.
    output_dir = PROJECT_ROOT / "evaluation_results"
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / f"{dataset_name}_results.json"

    output_path.write_text(
        json.dumps(report, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )

    print("\n" + "=" * 55)
    print(f"{dataset_name.upper()} EVALUATION SUMMARY")
    print("=" * 55)

    print(f"Total cases:       {summary['total_cases']}")
    print(f"Successful runs:   {successful_count}")
    print(f"Failed runs:       {failed_count}")
    print(f"Exact matches:     {exact_matches}")
    print(f"Exact match rate:  {summary['exact_match_rate']:.2%}")
    print(f"Precision:         {metrics['precision']:.2%}")
    print(f"Recall:            {metrics['recall']:.2%}")
    print(f"F1 score:          {metrics['f1']:.2%}")

    print(f"\nFull report saved to: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run V-Vet symptom extraction evaluation."
    )

    parser.add_argument(
        "--dataset",
        choices=["training", "validation", "test"],
        required=True,
        help="Dataset to evaluate.",
    )

    args = parser.parse_args()

    run_evaluation(args.dataset)
