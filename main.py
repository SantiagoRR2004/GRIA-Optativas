import pandas as pd
import markdownFunctions
import voting


def format_number(x: float) -> float:
    if pd.isna(x):
        return x  # Keep NaNs as is
    if x == int(x):
        return int(x)
    else:
        return x


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

    averagesDict = {
        "Asignatura": averages.index.tolist(),
        "Media": [format_number(x) for x in averages.values.tolist()],
        "Desviación típica": [format_number(x) for x in stdDevs.values.tolist()],
        "Mediana": [format_number(x) for x in medians.values.tolist()],
        "Moda": [format_number(x) for x in modes.values.tolist()],
        "Máximo": [format_number(x) for x in max.values.tolist()],
        "Mínimo": [format_number(x) for x in min.values.tolist()],
    }

    mainMarkdown.append(premade["statistics"])
    mainMarkdown.append(markdownFunctions.markdownTable(averagesDict))

    # Schulze method
    mainMarkdown.append(premade["schulze"])
    mainMarkdown.append(markdownFunctions.markdownTable(voting.schulze(df)))

    # Save the Markdown to a file
    with open("README.md", "w") as f:
        f.write("\n".join(mainMarkdown) + "\n")
