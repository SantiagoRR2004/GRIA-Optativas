import pandas as pd
import markdownFunctions

if __name__ == "__main__":

    csv_url = "https://docs.google.com/spreadsheets/d/1WvO5IBgJ3F6b6zHFQD5eWSxN-IUe3ONEvazHEUGb3Qo/export?format=csv"

    df = pd.read_csv(csv_url)

    # Remove the column called Marca temporal
    df = df.drop(columns=["Marca temporal"])

    # Load the different premade Markdown parts
    premade = markdownFunctions.loadMarkdownParts()
    mainMarkdown = [premade["beginning"]]

    # Average the values in each column
    averages = df.mean().round(2)

    # Sort the averages in descending order
    averages = averages.sort_values(ascending=False)

    averagesDict = {
        "Asignatura": averages.index.tolist(),
        "Media": averages.values.tolist(),
    }

    mainMarkdown.append(premade["average"])
    mainMarkdown.append(markdownFunctions.markdownTable(averagesDict))

    # Schulze method
    subjects = df.columns.tolist()

    # Step 1: Compute pairwise preferences
    pairwise = pd.DataFrame(index=subjects, columns=subjects)
    for i in range(len(subjects)):
        for j in range(len(subjects)):
            if i == j:
                pairwise.iloc[i, j] = 0
            else:
                pairwise.iloc[i, j] = df[subjects[i]].gt(df[subjects[j]]).sum()

    # Divide by the number of people that took both subjects
    for i in range(len(subjects)):
        for j in range(len(subjects)):
            if i != j:
                pairwise.iloc[i, j] /= (
                    df[[subjects[i], subjects[j]]].notna().all(axis=1).sum()
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

    schulzeDict = {
        "Asignatura": ranking_df["Subject"].tolist(),
    }

    mainMarkdown.append(premade["schulze"])
    mainMarkdown.append(markdownFunctions.markdownTable(schulzeDict))

    # Save the Markdown to a file
    with open("README.md", "w") as f:
        f.write("\n".join(mainMarkdown) + "\n")
