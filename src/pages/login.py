#  ______________________
#  Import LIBRARIES
from flet import (
    Column,
    ControlEvent,
    ElevatedButton,
    IconButton,
    Icons,
    Page,
    Text,
    TextField,
)
from collections.abc import Callable
#  Import FILES
#  ______________________


def create(on_login_success: Callable[[], None], page: Page) -> Column:
    def on_submit(e: ControlEvent) -> None:
        # add authentication logic
        username: str | None = username_input.value
        password: str | None = password_input.value
        if username == "admin" and password == "password":
            on_login_success()
        else:
            error_message.value = "Incorrect username or password! Try again."
            error_message.visible = True
            page.update()

    def toggle_password_visibility(e: ControlEvent) -> None:
        password_input.password = not password_input.password
        password_visibility_button.icon = (
            Icons.VISIBILITY if password_input.password else Icons.VISIBILITY_OFF
        )
        page.update()

    username_input: TextField = TextField(label="Username", width=200)
    password_input: TextField = TextField(
        label="Password", width=200, password=True, can_reveal_password=True
    )  # Added can_reveal_password for better UX
    password_visibility_button: IconButton = IconButton(
        icon=Icons.VISIBILITY, on_click=toggle_password_visibility
    )
    submit_button: ElevatedButton = ElevatedButton(text="login", on_click=on_submit)
    error_message: Text = Text(value="", color="red", visible=False)

    return Column(
        controls=[
            Text(value="Login Page", size=24),
            username_input,
            password_input,
            submit_button,
            error_message,
        ]
    )


# def create(on_login_success: Callable[[], None], page: ft.Page) -> Column:
#     def on_submit(e: ft.ControlEvent) -> None:
#         # add authentication logic
#         username: str | None = username_input.value
#         password: str | None = password_input.value
#         if username == "admin" and password == "password":
#             on_login_success()
#         else:
#             error_message.value = "Incorrect username or password! Try again."
#             error_message.visible = True
#             page.update()

#     def toggle_password_visibility(e: ft.ControlEvent) -> None:
#         password_input.password = not password_input.password
#         password_visibility_button.icon = (
#             Icons.VISIBILITY if password_input.password else Icons.VISIBILITY_OFF
#         )
#         page.update()

#     username_input: TextField = TextField(label="Username", width=200)
#     password_input: TextField = TextField(
#         label="Password", width=200, password=True, can_reveal_password=True
#     )  # Added can_reveal_password for better UX
#     show_password_checkbox: Checkbox = Checkbox(
#         label="Show Password", on_change=toggle_password_visibility
#     )
#     password_visibility_button: IconButton = IconButton(
#         icon=Icons.VISIBILITY, on_click=toggle_password_visibility
#     )
#     submit_button: ElevatedButton = ElevatedButton(text="login", on_click=on_submit)
#     error_message: Text = Text(value="", color="red", visible=False)

#     return Column(
#         controls=[
#             Text(value="Login Page", size=24),
#             username_input,
#             password_input,
#             submit_button,
#             error_message,
#         ]
#     )
