import pandas as pd
import markdownFunctions
import plotting
import voting


def format_number(x: float) -> float:
    if pd.isna(x):
        return x  # Keep NaNs as is
    if x == int(x):
        return int(x)
    else:
        return x


def main(df: pd.DataFrame) -> str:
    """
    Main function to process the DataFrame and generate the Markdown text.

    Args:
        - df (pd.DataFrame): The input DataFrame containing the data.
            Each column represents a subject.

    Returns:
        - str: The generated Markdown text.
    """
    # Load the different premade Markdown parts
    premade = markdownFunctions.loadMarkdownParts()
    mainMarkdown = [premade["beginning"]]

    # Average the values in each column
    averages = df.mean().round(2)

    # Sort the averages in descending order
    averages = averages.sort_values(ascending=False)

    # Standard deviation
    stdDevs = df.std().round(2)
    stdDevs = stdDevs[averages.index]
    # Median
    medians = df.median().round(2)
    medians = medians[averages.index]
    # Mode
    modes = df.mode().iloc[0].round(2)
    modes = modes[averages.index]
    # Maximum
    max = df.max().round(2)
    max = max[averages.index]
    # Minimum
    min = df.min().round(2)
    min = min[averages.index]
    # Number of students
    numStudents = df[averages.index].notna().sum()

    averagesDict = {
        "Asignatura": averages.index.tolist(),
        "Media": [format_number(x) for x in averages.values.tolist()],
        "Desviación típica": [format_number(x) for x in stdDevs.values.tolist()],
        "Mediana": [format_number(x) for x in medians.values.tolist()],
        "Moda": [format_number(x) for x in modes.values.tolist()],
        "Máximo": [format_number(x) for x in max.values.tolist()],
        "Mínimo": [format_number(x) for x in min.values.tolist()],
        "Número de alumnos": [format_number(x) for x in numStudents.tolist()],
    }

    mainMarkdown.append(premade["statistics"])
    mainMarkdown.append(markdownFunctions.markdownTable(averagesDict))

    # Probability distribution plot
    plotting.createProbabilityDistributionPlot(df)
    mainMarkdown.append(premade["distributions"])

    # Normal distribution plot
    plotting.createNormalDistributionPlot(df)
    mainMarkdown.append(premade["normalDistributions"])

    # Schulze method
    mainMarkdown.append(premade["schulze"])
    mainMarkdown.append(markdownFunctions.markdownTable(voting.schulze(df)))

    return "\n".join(mainMarkdown)


if __name__ == "__main__":

    csv_url = "https://docs.google.com/spreadsheets/d/1WvO5IBgJ3F6b6zHFQD5eWSxN-IUe3ONEvazHEUGb3Qo/export?format=csv"

    df = pd.read_csv(csv_url)

    # Remove the column called Marca temporal
    df = df.drop(columns=["Marca temporal"])

    # Divide the rows by year of the Original Timestamp
    df["Original Timestamp"] = pd.to_datetime(df["Original Timestamp"])
    year = {
        y: df[df["Original Timestamp"].dt.year == y].drop(
            columns=["Original Timestamp"]
        )
        for y in df["Original Timestamp"].dt.year.unique()
    }

    # Generate a README for each year
    for y, d in year.items():
        mainMarkdown = main(d)

        # Save the Markdown to a file
        with open(f"README{y}.md", "w") as f:
            f.write(mainMarkdown)

    # Remove the Original Timestamp column
    df = df.drop(columns=["Original Timestamp"])

    mainMarkdown = main(df)

    # Save the Markdown to a file
    with open("README.md", "w") as f:
        f.write(mainMarkdown)
