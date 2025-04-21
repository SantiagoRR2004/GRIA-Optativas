import pandas as pd

csv_url = "https://docs.google.com/spreadsheets/d/1WvO5IBgJ3F6b6zHFQD5eWSxN-IUe3ONEvazHEUGb3Qo/export?format=csv"

df = pd.read_csv(csv_url)
print(df.head())
