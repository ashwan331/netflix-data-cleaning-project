import pandas as pd
import mysql.connector
import numpy as np

# Load cleaned CSV
df = pd.read_csv("data/cleaned/netflix_cleaned.csv")

# Replace all NaN values with None
df = df.replace({np.nan: None})

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12943@a",
    database="netflix_project"
)

# Create cursor
cursor = conn.cursor()

# SQL query
query = """
INSERT INTO netflix_titles (
    show_id,
    type,
    title,
    director,
    cast,
    country,
    date_added,
    release_year,
    rating,
    duration,
    listed_in,
    description,
    year_added,
    month_added
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Insert rows safely
for row in df.itertuples(index=False, name=None):
    clean_row = tuple(None if pd.isna(x) else x for x in row)
    cursor.execute(query, clean_row)

# Commit changes
conn.commit()

print("Data inserted successfully!")

# Close connection
cursor.close()
conn.close()