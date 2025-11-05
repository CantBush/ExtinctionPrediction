import pandas as pd
import torch

print(torch.__version__)

# Load dataset
df = pd.read_csv("google_books_1299.csv")

# --- Search Function ---
def search_books(df):
    print("\nBook Search — type part of a title (or 'quit' to exit)\n")
    while True:
        query = input("Title: ").strip()
        if query.lower() == "quit":
            print("Goodbye!")
            break

        # Search for titles containing the query
        results = df[df["title"].str.contains(query, case=False, na=False)]

        if results.empty:
            print("No books found.\n")
            continue

        # Remove duplicate titles, just in case
        results = results.drop_duplicates(subset=["title"]) # have some duplicates, just have to clean it later

        if len(results) == 1:
            # Exactly one match → print full info
            row = results.iloc[0]
            print(f"Title: {row['title']}")
            print(f"Author: {row['author']}")
            print(f"Pages: {row['page_count']}")
            print(f"Rating: {row['rating']}")
            print(f"Publisher: {row.get('publisher', 'Unknown')}")
            print()

# --- Run search ---
search_books(df)