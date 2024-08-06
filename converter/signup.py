import flet as ft
from converter.router import go
from converter.scaffolder import *
from converter.database import Database

class SignUpScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        self.db = Database()

    def handle_signup(self, _):
        username = self.username_field.value
        password = self.password_field.value
        password_verification = self.password_verification_field.value

        if username and password:
            if password == password_verification:
                self.db.add_user(username, password)
            else:
                self.page.overlay.append(ft.SnackBar(ft.Text("Passwords don't match.")))
        else:
            self.page.overlay.append(ft.SnackBar(ft.Text("Please fill all fields.")))

    def handle_login(self, _):
        go(self.page, "login")

    def show(self):
        """Define o conteúdo do container usando funções pré-definidas (ver scaffolder.py)"""
        self.title = make_title("Sign up")
        self.username_field = make_text_field("User")
        self.password_field = make_password_field("Password")
        self.password_verification_field = make_password_field("Confirm Password")

        gradient_container = make_container(self.page, -1, 1)
        gradient_container.content = ft.Column(
            [
                ft.Text(),
                self.title,
                self.username_field,
                self.password_field,
                self.password_verification_field,
                ft.ElevatedButton("Sign up", on_click = self.handle_signup),
                ft.ElevatedButton("Log in", on_click = self.handle_login),
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing=50,
        )

        self.page.add(gradient_container)
