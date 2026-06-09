import pandas as pd

# Load dataset
df = pd.read_csv("data/raw_data.csv")

print("Original Dataset:")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Unknown")

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Save cleaned dataset
df.to_csv("data/cleaned_data.csv", index=False)

print("\nCleaned Dataset:")
print(df)

print("\nData Cleaning Completed Successfully!")
