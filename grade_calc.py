"""Interactive grade calculator with editable component table.

Each component has a course weight percent and raw points possible.
The script asks for your earned raw points, computes weighted contribution,
and compares your current weighted score to class average/std dev.
"""

CLASS_AVERAGE = 24.08
CLASS_STD_DEV = 2.42

# Grade Table.
components = [
    {"name": "Test 1", "weight_percent": 12, "points_possible": 60},
    {"name": "Pop-Quizzes", "weight_percent": 5, "points_possible": 10},
    {"name": "Project - Phase 2", "weight_percent": 12, "points_possible": 200},
    {"name": "Preliminary Homework", "weight_percent": 2, "points_possible": 20},
]


def prompt_score(label: str, max_points: float) -> float:
    """Prompt repeatedly until the user enters a valid score in range."""
    while True:
        raw = input(f"Enter your score for {label} (0-{max_points}): ").strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a numeric value.")
            continue

        if value < 0 or value > max_points:
            print(f"Score must be between 0 and {max_points}.")
            continue

        return value


def letter_grade(x_percent: float, avg_percent: float, std_percent: float) -> str:
    """Return letter grade using the provided mean/std-dev cutoffs."""
    if x_percent >= (avg_percent + 0.25 * std_percent):
        return "A"
    if (avg_percent - 2 * std_percent) <= x_percent < (avg_percent + 0.25 * std_percent):
        return "B"
    if (avg_percent - 4 * std_percent) <= x_percent < (avg_percent - 2 * std_percent):
        return "C"
    if (avg_percent - 6 * std_percent) <= x_percent < (avg_percent - 4 * std_percent):
        return "D"
    return "F"


def main() -> None:
    total_weight = sum(item["weight_percent"] for item in components)
    print(f"Current Grade Calculator (configured weights total {total_weight:.2f}%)")
    print("Enter raw points earned for each item.\n")

    weighted_total = 0.0
    print("Breakdown:")
    for item in components:
        name = item["name"]
        weight = float(item["weight_percent"])
        possible = float(item["points_possible"])

        earned = prompt_score(name, possible)
        raw_percent = (earned / possible) if possible > 0 else 0.0
        weighted_contribution = raw_percent * weight
        weighted_total += weighted_contribution

        print(
            f"- {name}:({raw_percent * 100:.2f}%)"
        )

    normalized_percent = (weighted_total / total_weight) * 100 if total_weight > 0 else 0.0

    print("\n--- Results ---")
    print(f"Current weighted score: {weighted_total:.2f} / {total_weight:.2f}")
    print(f"Current normalized percentage: {normalized_percent:.2f}%")

    # Convert class stats to percent scale so x is in 0..100.
    avg_percent = (CLASS_AVERAGE / total_weight) * 100 if total_weight > 0 else 0.0
    std_percent = (CLASS_STD_DEV / total_weight) * 100 if total_weight > 0 else 0.0

    diff = normalized_percent - avg_percent
    z_score = diff / std_percent if std_percent != 0 else 0.0
    grade = letter_grade(normalized_percent, avg_percent, std_percent)

    print("\nClass comparison (editable via CLASS_AVERAGE and CLASS_STD_DEV):")
    print(f"- Class average (percent): {avg_percent:.2f}%")
    print(f"- Std. Dev. (percent): {std_percent:.2f}%")
    print(f"- Your letter grade by curve rule: {grade}")
    print(f"- Z-score: {z_score:.2f}")




if __name__ == "__main__":
    main()
