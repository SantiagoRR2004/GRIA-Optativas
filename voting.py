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
    pairwise = pairwisePreferences(data)

    # Divide by the number of people that took both subjects
    for i in range(len(subjects)):
        for j in range(len(subjects)):
            if i != j:
                pairwise.iloc[i, j] /= (
                    data[[subjects[i], subjects[j]]].notna().all(axis=1).sum()
                )

    # Step 2: Compute strongest paths
    strength = strongestPath(pairwise)

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


def pairwisePreferences(data: pd.DataFrame) -> pd.DataFrame:
    """
    Compute pairwise preferences from a DataFrame of values.

    For (row, column) in the DataFrame, the value represents the number of
    voters who prefer the option in the row over the option in the column.

    Args:
        - data (pd.DataFrame): DataFrame containing grades for different subjects.
            Each column represents an option, and each row represents a voter.

    Returns:
        - pd.DataFrame: A DataFrame containing pairwise preferences.
    """
    options = data.columns.tolist()
    pairwise = pd.DataFrame(index=options, columns=options)

    for i in range(len(options)):
        for j in range(len(options)):
            if i == j:
                pairwise.iloc[i, j] = 0
            else:
                pairwise.iloc[i, j] = data[options[i]].gt(data[options[j]]).sum()

    return pairwise


def strongestPath(data: pd.DataFrame) -> pd.DataFrame:
    """
    Compute the strongest path between each pair of options in a DataFrame.
    The Floyd-Warshall algorithm is used to find the strongest paths and
    higher values indicate stronger preferences.

    Args:
        - data (pd.DataFrame): DataFrame containing pairwise preferences.

    Returns:
        - pd.DataFrame: A DataFrame containing the strongest paths.
    """
    options = data.columns.tolist()
    strength = data.copy()

    for i in options:
        for j in options:
            if i != j:
                for k in options:
                    if i != k and j != k:
                        strength.at[j, k] = max(
                            strength.at[j, k], min(strength.at[j, i], strength.at[i, k])
                        )

    return strength
