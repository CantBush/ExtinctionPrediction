import flet as ft
import pandas as pd

FILE_PATH = "google_books_cleaned.csv"

def main(page: ft.Page):
    # Set the title of the Flet application window/tab
    page.title = "Name here"

    # Add Text on screen
    page.add(
        ft.Text("Name here", size=30, weight=ft.FontWeight.BOLD)
    )

ft.app(target=main,view=ft.WEB_BROWSER, port=8550)
# Running on http://localhost:8550