#  ______________________
#  Import LIBRARIES
import flet as ft
from flet import Page, app

#  Import FILES
from components import header, footer
from pages import home, login
#  ______________________


def main(page: Page) -> None:
    # Your UI elements and logic go here
    page.title = "Login example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def show_login_page() -> None:
        page.clean()
        page.add(login.create(on_login_success=on_login_success, page=page))

    def on_login_success() -> None:
        page.clean()
        page.add(header.create())
        page.add(home.create())
        page.add(footer.create())

    show_login_page()


if __name__ == "__main__":
    app(target=main)


#  ______________________
#  Import LIBRARIES
#  Import FILES
#  ______________________
