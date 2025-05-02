from typing import List, Dict


def markdownTable(data: Dict[str, List[object]]) -> str:
    """
    Convert a dictionary to a markdown table.

    Args:
        - data (dict): The dictionary to convert.
            The keys will be the column headers and the values will be the data.
            The values should be lists of the same length.
            Each list represents a column in the table.

    Returns:
        - str: The markdown table as a string.
    """
    # Get the keys and values from the dictionary
    keys = list(data.keys())
    values = list(data.values())

    # Start the markdown table
    rows = []

    # Create the header row
    header = (
        " ".join([f'| <img width="1000"><br><p align="center">{key} ' for key in keys])
        + "|"
    )
    rows.append(header)

    n = len(keys)

    if n == 1:
        separator = "|:--:|"
    elif n == 2:
        separator = "|:--|--:|"
    else:
        separator = "|:--|" + "|".join([":--:" for _ in range(n - 2)]) + "|--:|"
    rows.append(separator)

    # Create the data rows
    dataRows = []
    for row in zip(*values):
        data_row = " ".join([f"| {value} " for value in row]) + "|"
        dataRows.append(data_row)
        rows.append(data_row)

    return "\n".join(rows)
