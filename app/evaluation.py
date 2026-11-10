
def calculate_metrics(expected_cases, actual_cases):
    """
    Calculate micro-averaged precision, recall and F1
    across sign/value pairs.

    A wrong value counts as both a false positive
    and a false negative.
    """

    if len(expected_cases) != len(actual_cases):
        raise ValueError(
            "Expected and actual case counts must match."
        )

    true_positive = 0
    false_positive = 0
    false_negative = 0

    for expected, actual in zip(expected_cases, actual_cases):
        all_signs = set(expected) | set(actual)

        for sign in all_signs:
            expected_value = expected.get(sign)
            actual_value = actual.get(sign)

            if expected_value is not None and actual_value is not None:
                if expected_value == actual_value:
                    true_positive += 1
                else:
                    false_positive += 1
                    false_negative += 1

            elif actual_value is not None:
                false_positive += 1

            elif expected_value is not None:
                false_negative += 1

    precision = (
        true_positive / (true_positive + false_positive)
        if true_positive + false_positive else 0
    )

    recall = (
        true_positive / (true_positive + false_negative)
        if true_positive + false_negative else 0
    )

    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall else 0
    )

    return {
        "true_positive": true_positive,
        "false_positive": false_positive,
        "false_negative": false_negative,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4)
    }
