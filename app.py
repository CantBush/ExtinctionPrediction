import flet as ft
import pandas as pd

FILE_PATH = "google_books_cleaned.csv"

def main(page: ft.Page):
    # Set the title of the Flet application window/tab
    page.title = "Name here"

    # Center everything on the page
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Title text
    title = ft.Text(
        "Name here",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    # Search bar
    search_bar = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.Colors.AMBER,
        bar_hint_text="Search for a book...",
        width=400,  # Optional: sets a nice width for the bar
    )

    # Add both to the page inside a vertically centered Column
    page.add(
        ft.Column(
            [
                title,
                ft.Container(height=20),  # small space between title and bar
                search_bar,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
# Running on http://localhost:8550