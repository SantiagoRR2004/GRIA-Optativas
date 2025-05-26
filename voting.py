from itertools import combinations
from typing import List, Dict
import pandas as pd
import copy


def schulze(data: pd.DataFrame) -> Dict[str, List]:
    """
    Calculate the Schulze method ranking for a given DataFrame of grades.
    The DataFrame should have subjects as columns and grades as values.

    It is an iterative process that once it finds
    the subject with the highest preference, it removes it from the DataFrame
    and repeats the process until all subjects are ranked.

    This also normalizes the pairwise preferences by dividing
    the number of voters who prefer one subject over another by the number
    of voters who took both subjects.

    Args:
        - data (pd.DataFrame): DataFrame containing grades for different subjects.
            Each column represents a subject, and each row represents a student.

    Returns:
        - Dict[str, List]: A dictionary containing the ranking of subjects based on
            the Schulze method. The key is "Asignatura" and the values
            the subjects in order of preference.
    """
    data = copy.deepcopy(data)
    averages = list(data.mean().round(2).sort_values(ascending=False).index)
    subjects = data.columns.tolist()
    ranking = []

    while len(ranking) < len(subjects):
        # Step 1: Compute pairwise preferences
        pairwise = pairwisePreferences(data)

        # Divide by the number of people that took both subjects
        columns = data.columns.tolist()
        for i in range(len(columns)):
            for j in range(len(columns)):
                if i != j:
                    pairwise.iloc[i, j] /= (
                        data[[columns[i], columns[j]]].notna().all(axis=1).sum()
                    )

        # Step 2: Compute strongest paths
        strength = strongestPath(pairwise)

        # Step 3: Get the winner
        winner = getCondorcetWinner(strength, averages)
        ranking.append(winner)
        data.drop(columns=winner, inplace=True)

    return {"Asignatura": ranking}


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
    strengths = copy.deepcopy(data)

    for i in options:
        for j in options:
            if i != j:
                for k in options:
                    if i != k and j != k:
                        strengths.at[j, k] = max(
                            strengths.at[j, k],
                            min(strengths.at[j, i], strengths.at[i, k]),
                        )

    return strengths


def getCondorcetWinner(strengths: pd.DataFrame, tiebreaker: List[str]) -> str:
    """
    Find the Condorcet winner from a pairwise preference matrix.
    A Condorcet winner is an option that beats all other options in pairwise comparisons.

    Args:
        - strengths (pd.DataFrame): A DataFrame representing pairwise preferences.
            The values indicate the number of voters who prefer one option over another.
        - tiebreaker (List[str]): A list of options to use as a tiebreaker if no Condorcet winner is found.

    Returns:
        - str: The Condorcet winner, or the first option from the tiebreaker list if no winner is found.
    """
    strengths = copy.deepcopy(strengths)
    options = strengths.columns.tolist()
    strongest = None

    # We find if any option beats all others
    for op in options:
        if all(strengths.at[op, j] > strengths.at[j, op] for j in options if op != j):
            strongest = op
            break

    # If no option beats all others, we use the tiebreaker
    if not strongest:
        cycle = findWinnersCycle(strengths)
        print(f"Found cycle with: {cycle}")

        # Get the option that appears first in the tiebreaker list
        for op in tiebreaker:
            if op in cycle:
                strongest = op
                break

    return strongest


def findWinnersCycle(matrix: pd.DataFrame) -> List[str]:
    """
    Find a cycle of winners in a pairwise preference matrix.
    It finds the smallest subset of candidates such that each candidate
    in the subset defeats all candidates outside the subset.

    Args:
        - matrix (pd.DataFrame): A DataFrame representing pairwise preferences.
            The values indicate the number of voters who prefer one option over another.

    Returns:
        - List[str]: A list of candidates forming a cycle, or an empty list if no cycle is found.
    """
    candidates = matrix.index.tolist()

    def defeats(i, j):
        return matrix.loc[i, j] > matrix.loc[j, i]

    n = len(candidates)

    # Try subsets of increasing size
    for size in range(1, n + 1):
        for subset in combinations(candidates, size):
            subset_set = set(subset)
            defeats_all_outside = True
            for i in subset:
                for j in candidates:
                    if j not in subset_set and not defeats(i, j):
                        defeats_all_outside = False
                        break
                if not defeats_all_outside:
                    break
            if defeats_all_outside:
                return list(subset)

    return []  # No winners found (unlikely if input is valid)
