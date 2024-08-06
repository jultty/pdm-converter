import flet as ft

def make_container(page, horizontalAlignment, verticalAlignment):
    """Retorna um container com fundo em gradiente e alinhamento centralizado

    Argumentos:
    page -- página atual
    horizontalAlignment -- alinhamento horizontal, invertido para o fim do gradiente
    verticalAlignment -- alinhamento vertical, invertido para o fim do gradiente
    """
    return ft.Container(
    width = page.window.width,
    height = page.window.height,
    gradient = ft.LinearGradient(
        colors = ["#049578", "#AF87FF"],
        begin = ft.Alignment(horizontalAlignment, verticalAlignment),
        end = ft.Alignment(verticalAlignment, horizontalAlignment)
    )
)

def make_title(text):
    """Retorna um elemento de texto em tamanho grande

    Argumentos:
    text -- Texto para exibir como título
    """
    return ft.Text(value = text,
            theme_style = ft.TextThemeStyle.DISPLAY_LARGE,
            color = ft.colors.WHITE,
            )

def make_text_field(label):
    """Retorna um campo de texto

    Argumentos:
    label -- Texto para identificação do campo pela pessoa usuária
    """
    return ft.TextField(
        label = label,
        width = 300,
        color = ft.colors.WHITE,
        border_color = ft.colors.WHITE,
        label_style = ft.TextStyle(color="#ffffff"),
        helper_style = ft.TextStyle(color="#ffffff"),
        hint_style = ft.TextStyle(color="#888888"),
        autofocus = True,
    )

def make_password_field(label):
    """Retorna um campo de senha com botão para exibir o conteúdo

    Argumentos:
    label -- Texto para identificação do campo pela pessoa usuária
    """
    return ft.TextField(
        label = label,
        width = 300,
        color = ft.colors.WHITE,
        border_color = ft.colors.WHITE,
        label_style = ft.TextStyle(color="#ffffff"),
        helper_style = ft.TextStyle(color="#ffffff"),
        hint_style = ft.TextStyle(color="#888888"),
        password = True,
        can_reveal_password = True,
        autofocus = True,
    )

def make_navigation(page, left_label, left_target, right_label, right_target):
    """Retorna um menu de navegação centralizado com dois botões

    Argumentos:
    page -- página atual
    left_label -- Texto para ser exibido no botão do lado esquerdo
    left_target -- Uma função para ser executada ao clicar no botão esquerdo
    right_label -- Texto para ser exibido no botão do lado direito
    right_target -- Uma função para ser executada ao clicar no botão direito
    """
    return ft.Row([
        ft.ElevatedButton(
            text = left_label,
            bgcolor="#ffffff",
            color="#000000",
            on_click = left_target,
        ),
        ft.ElevatedButton(
            text = right_label,
            bgcolor="#ffffff",
            color="#000000",
            on_click = right_target,
        ),
    ], width = page.width, alignment = ft.MainAxisAlignment.CENTER)
