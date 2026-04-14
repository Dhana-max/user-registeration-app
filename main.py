import flet as ft
from logic import process_user

def main(page: ft.Page):
    page.title = "My First Application"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    title = ft.Text("User Registration", size=24, weight=ft.FontWeight.BOLD)

    name_input = ft.TextField(label="Name", width=300)
    age_input = ft.TextField(label="Age", width=300, keyboard_type=ft.KeyboardType.NUMBER)

    error_text = ft.Text(color=ft.Colors.RED)
    result_text = ft.Text()

    def on_submit(e):
        error_text.value = ""
        result_text.value = ""

        if not name_input.value.strip():
            error_text.value = "Name is required"
        elif not age_input.value.isdigit():
            error_text.value = "Age must be a number"
        else:
            result_text.value = process_user(name_input.value, int(age_input.value))

        page.update()

    submit_button = ft.ElevatedButton("Submit", on_click=on_submit)

    page.add(
        ft.Column(
            [
                title,
                name_input,
                age_input,
                submit_button,
                error_text,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
