import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Netflix Data Analytics Dashboard")

# Load dataset
df = pd.read_csv("data/cleaned/netflix_cleaned.csv")

# -----------------------------
# Total Titles
# -----------------------------
st.subheader("Total Titles")

st.write(df.shape[0])

# -----------------------------
# Movies vs TV Shows
# -----------------------------
st.subheader("Movies vs TV Shows")

type_counts = df['type'].value_counts()

fig1, ax1 = plt.subplots()

ax1.pie(
    type_counts.values,
    labels=type_counts.index,
    autopct='%1.1f%%'
)

st.pyplot(fig1)

# -----------------------------
# Top 10 Countries
# -----------------------------
st.subheader("Top 10 Countries")

top_countries = df['country'].value_counts().head(10)

fig2, ax2 = plt.subplots(figsize=(10,5))

ax2.bar(
    top_countries.index,
    top_countries.values
)

plt.xticks(rotation=45)

st.pyplot(fig2)

# -----------------------------
# Ratings Distribution
# -----------------------------
st.subheader("Ratings Distribution")

rating_counts = df['rating'].value_counts()

fig3, ax3 = plt.subplots(figsize=(10,5))

ax3.bar(
    rating_counts.index,
    rating_counts.values
)

plt.xticks(rotation=45)

st.pyplot(fig3)

# -----------------------------
# Content Added Per Year
# -----------------------------
st.subheader("Content Added Per Year")

year_data = (
    df['year_added']
    .dropna()
    .astype(int)
    .value_counts()
    .sort_index()
)

fig4, ax4 = plt.subplots(figsize=(10,5))

ax4.plot(
    year_data.index,
    year_data.values
)

st.pyplot(fig4)