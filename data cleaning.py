import pandas as pd

# Load the dataset
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Netflix TV Shows and Movies.csv")

# Drop redundant index column
df.drop(columns=["index"], inplace=True)

# Fill missing values
df['description'].fillna("Not Available", inplace=True)
df['age_certification'].fillna("Unrated", inplace=True)
df['imdb_votes'].fillna(0, inplace=True)

# Convert data types (if needed)
df['imdb_votes'] = df['imdb_votes'].astype(int)

# Optional: Create a new column for decade analysis
df['decade'] = (df['release_year'] // 10) * 10

# Save cleaned file for Power BI
df.to_csv("Cleaned_Netflix_IMDB.csv", index=False)
print(df)
