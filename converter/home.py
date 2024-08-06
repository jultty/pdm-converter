import flet as ft
import converter
from converter.scaffolder import *
from converter.router import go


class HomeScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        self.db = converter.Database()
        self.output = make_output_field()
        self.title = make_title("Converter")

        self.input = make_text_field("Value")
        self.input.max_length = 8
        self.input.on_change = self.handle_input_change
        self.input.input_filter = ft.NumbersOnlyInputFilter()

        self.visualization = ft.GridView(
            runs_count=6,
            max_extent=120,
            child_aspect_ratio=1.0,
            spacing=3,
            run_spacing=3,
        )

    def handle_logout(self, _):
        go(self.page, "login")

    def handle_input_change(self, e):
        if self.input.value:
            self.output.value = bin(int(self.input.value)).replace("0b", "", 1)

        places = []
        p = 1
        for c in str(self.output.value):
            places.append(p)
            p = p * 2

        places = places[::-1]

        bg_color = ""
        text_size = 20
        self.visualization.controls.clear()
        for i, c in enumerate(str(self.output.value)):

            if c == "0":
                bg_color = ft.colors.with_opacity(0.4, ft.colors.GREY)
            else:
                bg_color = ft.colors.with_opacity(0.4, ft.colors.TEAL_700)

            if int(places[i]) > 99999:
                text_size = 10
            elif int(places[i]) > 999:
                text_size = 15

            self.visualization.controls.append(
                ft.Container(
                    content = ft.Text(
                        f"{c} x {places[i]}",
                        size = text_size,
                        color=ft.colors.WHITE,
                    ),
                    alignment = ft.alignment.center,
                    bgcolor = bg_color,
                    margin = 10,
                    border_radius = 20,
                )
            )

        e.page.update()

    def show(self):
        gradient_container = make_container(self.page, 1, -1)
        gradient_container.content = ft.Column(
            [
                ft.Text(),
                self.title,
                self.input,
                self.visualization,
                self.output,
                ft.ElevatedButton("Log in", on_click = self.handle_logout)
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            spacing=50,
        )

        self.page.add(gradient_container)
