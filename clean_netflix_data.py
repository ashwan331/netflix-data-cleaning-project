import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data/raw/netflix_titles.csv")

# Display first 5 rows
print(df.head())

# Check dataset shape
print(df.shape)

# Check null values
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')

# Remove rows where rating is missing
df.dropna(subset=['rating'], inplace=True)

# Remove extra spaces from date column
df['date_added'] = df['date_added'].str.strip()

# Convert date column to datetime
df['date_added'] = pd.to_datetime(
    df['date_added'],
    errors='coerce'
)

# Create new columns
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

# Standardize text values
df['type'] = df['type'].str.upper()

# Fill missing duration values
df['duration'] = df['duration'].fillna('Unknown')

# Final dataset info
print("\nCleaned Dataset Info:")
print(df.info())

# Save cleaned dataset
df.to_csv(
    "data/cleaned/netflix_cleaned.csv",
    index=False
)

print("\nData cleaned successfully!")
print("Cleaned file saved at: data/cleaned/netflix_cleaned.csv")