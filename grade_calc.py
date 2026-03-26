"""Interactive grade calculator with editable component table.

Each component has a course weight percent and raw points possible.
The script asks for your earned raw points, computes weighted contribution,
and compares your current weighted score to class average/std dev.
"""

# Class Stats.
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
    #print(f"Current normalized percentage: {normalized_percent:.2f}%")

    diff = weighted_total - CLASS_AVERAGE
    z_score = diff / CLASS_STD_DEV if CLASS_STD_DEV != 0 else 0.0
    relation = "above" if diff > 0 else "below" if diff < 0 else "equal to"

    print("\nClass comparison (editable via CLASS_AVERAGE and CLASS_STD_DEV):")
    print(f"- Class average: {CLASS_AVERAGE:.2f}")
    print(f"- Std. Dev.: {CLASS_STD_DEV:.2f}")
    if relation == "equal to":
        print("- You are exactly at the class average.")
    else:
        print(f"- You are {abs(diff):.2f} points {relation} average.")
    print(f"- Z-score: {z_score:.2f}")


if __name__ == "__main__":
    main()
