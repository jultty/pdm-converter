import converter

def go(page, target):
    page.clean()

    if target == "signup":
        converter.SignUpScreen(page).show()
    elif target == "home":
        converter.HomeScreen(page).show()
    elif target == "login":
        converter.LoginScreen(page).show()
