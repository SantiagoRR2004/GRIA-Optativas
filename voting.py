from typing import List, Dict
import pandas as pd


def schulze(data: pd.DataFrame) -> Dict[str, List]:
    """
    Calculate the Schulze method ranking for a given DataFrame of grades.
    The DataFrame should have subjects as columns and grades as values.

    Args:
        - data (pd.DataFrame): DataFrame containing grades for different subjects.
            Each column represents a subject, and each row represents a student.

    Returns:
        - Dict[str, List]: A dictionary containing the ranking of subjects based on
            the Schulze method. The key is "Asignatura" and the values
            the subjects in order of preference.
    """
    averages = data.mean().round(2).sort_values(ascending=False)
    subjects = data.columns.tolist()

    # Step 1: Compute pairwise preferences
    pairwise = pd.DataFrame(index=subjects, columns=subjects)
    for i in range(len(subjects)):
        for j in range(len(subjects)):
            if i == j:
                pairwise.iloc[i, j] = 0
            else:
                pairwise.iloc[i, j] = data[subjects[i]].gt(data[subjects[j]]).sum()

    # Divide by the number of people that took both subjects
    for i in range(len(subjects)):
        for j in range(len(subjects)):
            if i != j:
                pairwise.iloc[i, j] /= (
                    data[[subjects[i], subjects[j]]].notna().all(axis=1).sum()
                )

    # Step 2: Compute strongest paths using Floyd-Warshall
    strength = pairwise.copy()

    for i in subjects:
        for j in subjects:
            if i != j:
                for k in subjects:
                    if i != k and j != k:
                        strength.at[j, k] = max(
                            strength.at[j, k], min(strength.at[j, i], strength.at[i, k])
                        )

    # Step 3: Identify the order of subjects
    # TODO: Use topological sorting
    def beats(x, y):
        return strength.at[x, y] > strength.at[y, x]

    victories = {x: sum(beats(x, y) for y in subjects if x != y) for x in subjects}

    # Step 4: Combine into DataFrame
    ranking_df = pd.DataFrame(
        {
            "Subject": subjects,
            "Victory Count": [victories[x] for x in subjects],
            "Average Grade": [averages[x] for x in subjects],
        }
    )

    # Step 5: Sort by victory count, then by average grade
    ranking_df = ranking_df.sort_values(
        by=["Victory Count", "Average Grade"], ascending=False
    ).reset_index(drop=True)

    return {
        "Asignatura": ranking_df["Subject"].tolist(),
    }
