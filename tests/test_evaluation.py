
import pytest

from app.evaluation import calculate_metrics


def test_perfect_predictions():
    expected = [{"ticks": "yes", "weakness": "no"}]
    actual = [{"ticks": "yes", "weakness": "no"}]

    metrics = calculate_metrics(expected, actual)

    assert metrics["precision"] == 1.0
    assert metrics["recall"] == 1.0
    assert metrics["f1"] == 1.0


def test_wrong_prediction():
    expected = [{"ticks": "yes"}]
    actual = [{"ticks": "no"}]

    metrics = calculate_metrics(expected, actual)

    assert metrics["true_positive"] == 0
    assert metrics["false_positive"] == 1
    assert metrics["false_negative"] == 1


def test_missing_finding():
    expected = [{"ticks": "yes"}]
    actual = [{}]

    metrics = calculate_metrics(expected, actual)

    assert metrics["false_negative"] == 1
    assert metrics["recall"] == 0.0


def test_extra_finding():
    expected = [{}]
    actual = [{"ticks": "yes"}]

    metrics = calculate_metrics(expected, actual)

    assert metrics["false_positive"] == 1
    assert metrics["precision"] == 0.0


def test_mismatched_case_counts_are_rejected():
    with pytest.raises(ValueError):
        calculate_metrics([{"ticks": "yes"}], [])
