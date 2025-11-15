import flet as ft
import pandas as pd

FILE_PATH = "google_books.csv"

def main(page: ft.Page):
    # Set the title of the Flet application window/tab
    page.title = "Name here"

    # Center everything on the page
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Load dataset
    df = pd.read_csv(FILE_PATH)

    # Output area where we will show book info
    output = ft.Column(spacing=10)

    # Title text
    title = ft.Text(
        "Name here",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    # Search handler
    def search_book(e):
        query = search_bar.value.strip()

        if query == "":
            output.controls = [ft.Text("Please enter a title.", color="red")]
            page.update()
            return

        # Filter dataset
        results = df[df["title"].str.contains(query, case=False, na=False)]

        if results.empty:
            output.controls = [ft.Text("No books found.", color="red")]
        else:
            # Only show the first match
            row = results.iloc[0]

            output.controls = [
                ft.Text(f"Title: {row['title']}", size=18, weight="bold"),
                ft.Text(f"Author: {row['authors']}"),
                ft.Text(f"Pages: {row['pageCount']}"),
                ft.Text(f"Rating: {row.get('averageRating', 'N/A')}"),
                ft.Text(f"Publisher: {row.get('publisher', 'Unknown')}"),
            ]

        page.update()

    # Search bar
    search_bar = ft.SearchBar(
        bar_hint_text="Search for a book...",
        width=400,
        on_submit=search_book,   # Connect search function
    )

    # Add both to the page inside a vertically centered Column
    page.add(
        ft.Column(
            [
                ft.Text("name...", size=30, weight=ft.FontWeight.BOLD),
                ft.Container(height=20),
                search_bar,
                ft.Container(height=30),
                output,    # results appear here
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
# Running on http://localhost:8550