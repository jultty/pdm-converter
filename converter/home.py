import flet as ft
import converter
from converter.scaffolder import *
from converter.router import go


class HomeScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        self.db = converter.Database()

    def handle_logout(self, _):
        go(self.page, "login")

    def show(self):
        self.title = make_title("Converter")

        gradient_container = make_container(self.page, 1, -1)
        gradient_container.content = ft.Column(
            [
                self.title,
                ft.ElevatedButton("Log in", on_click = self.handle_logout)
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing=50,
        )

        self.page.add(gradient_container)
