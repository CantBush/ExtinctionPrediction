import pandas as pd

# === Load the dataset ===
file_path = "google_books_dataset.csv"
df = pd.read_csv(file_path)

print("Before cleaning:")
print(f"Rows: {len(df)}")
print(f"Columns: {list(df.columns)}\n")

# === 1. Remove duplicates ===
df = df.drop_duplicates()
print(f"After removing duplicates: {len(df)} rows\n")

# === 2. Check for missing values ===
print("Missing values per column:")
print(df.isnull().sum())
print("\n")

# save as new cleaned file
df.to_csv("google_books.csv", index=False)

print("Cleaning complete!")
print("Saved as 'google_books_cleaned.csv'")

