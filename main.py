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

    # Save the Markdown to a file
    with open("README.md", "w") as f:
        f.write("\n".join(mainMarkdown) + "\n")
