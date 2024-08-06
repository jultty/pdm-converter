import flet as ft

from converter.router import go

def main(page: ft.Page):
    """
    Função principal
    Serve como ponto de entrada da aplicação

    Argumentos:
    page: Página atual (suprido automaticamente pelo Flet)
    """

    go(page, "login")

ft.app(target=main)
