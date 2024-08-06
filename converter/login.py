import flet as ft
from converter.router import go
from converter.database import Database
from converter.scaffolder import *

class LoginScreen:
    """
    Define a view LoginView da rota "/login"

    Argumentos:
    page: Página atual (suprido automaticamente pelo Flet)
    """
    def __init__(self, page: ft.Page):
        self.page = page
        self.db = Database()

    def handle_login(self, _):
        username = self.username_field.value
        password = self.password_field.value

        db_password = self.db.get_password(username)

        print("input password:", password)
        print("db password:", db_password)
        if password == db_password:
            go(self.page, "home")
        else:
            self.page.overlay.append(ft.SnackBar(ft.Text("Please fill all fields")))


    def handle_signup(self, _):
        go(self.page, "signup")

    def show(self):
        """Define o conteúdo do container usando funções pré-definidas (ver scaffolder.py)"""
        self.title = make_title("Log in")
        self.username_field = make_text_field("User")
        self.password_field = make_password_field("Password")

        """Cria um container com gradiente (ver scaffolder.py)"""
        gradient_container = make_container(self.page, 1, -1)
        gradient_container.content = ft.Column(
            [
                ft.Text(),
                self.title,
                self.username_field,
                self.password_field,
                ft.ElevatedButton("Log in", on_click = self.handle_login),
                ft.ElevatedButton("Sign up", on_click = self.handle_signup),
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing=50,
        )

        """Retorna a view para a rota "/" contendo o gradient_container definido acima"""
        self.page.add(gradient_container)
