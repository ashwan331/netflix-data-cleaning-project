import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/cleaned/netflix_cleaned.csv")

# Style
sns.set_style("darkgrid")

# -----------------------------
# Clean important columns
# -----------------------------
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')
df['year_added'] = pd.to_numeric(df['year_added'], errors='coerce')

# -----------------------------
# 1. Movies vs TV Shows
# -----------------------------
plt.figure(figsize=(6,6))

df['type'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Movies vs TV Shows")
plt.ylabel("")

plt.savefig("movies_vs_tvshows.png")
plt.close()

# -----------------------------
# 2. Top 10 Countries
# -----------------------------
plt.figure(figsize=(12,6))

top_countries = df['country'].value_counts().head(10)

plt.bar(
    top_countries.index,
    top_countries.values
)

plt.xticks(rotation=45)

plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("top_countries.png")
plt.close()

# -----------------------------
# 3. Ratings Distribution
# -----------------------------
plt.figure(figsize=(12,6))

rating_counts = df['rating'].value_counts()

plt.bar(
    rating_counts.index,
    rating_counts.values
)

plt.xticks(rotation=45)

plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("ratings_distribution.png")
plt.close()

# -----------------------------
# 4. Content Added Per Year
# -----------------------------
plt.figure(figsize=(12,6))

year_data = (
    df['year_added']
    .dropna()
    .astype(int)
    .value_counts()
    .sort_index()
)

plt.plot(
    year_data.index,
    year_data.values
)

plt.title("Content Added Per Year")
plt.xlabel("Year")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("content_per_year.png")
plt.close()

print("All visualizations created successfully!")