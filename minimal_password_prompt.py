# minimal_password_prompt.py

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Center, Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Header, Input

class PasswordPromptDialog(ModalScreen):

    DEFAULT_CSS = """
    PasswordPromptDialog {
        align: center middle;
        background: $primary 30%;
        }

        #minimal-pw-dlg {
            width: 85;
            height: 18;
            border: thick $background 70%;
            content-align: center middle;
            margin: 1;
        }

        Button {
            width: 50%;
            margin: 1;
        }
    """

    def __init__(self) -> None:
        super().__init__()
        self.title = "Enter Password"

    def compose(self):
        yield Vertical(
            Header(),
            Center(Input(placeholder="Enter password:", password=True, id="minimal-pw")),
            Center(
                Horizontal(
                     Button("OK", variant="primary", id="minimal-pw-ok"),
                     Button("Cancel", variant="error", id="minimal-pw-cancel"),
                )
            ),
            id="minimal-pw-dlg",
        )

    @on(Button.Pressed, "#minimal-pw-ok")
    def on_ok(self, event: Button.Pressed) -> None:
        """
        Return the user's choice back to the calling application and dismiss the dialog
        """
        value = self.query_one("#minimal-pw").value
        self.dismiss(value)

    @on(Button.Pressed, "#minimal-pw-cancel")
    def on_cancel(self, event: Button.Pressed) -> None:
        """
        Returns False to the calling application and dismisses the dialog
        """
        self.dismiss(False)

class PasswordPromptApp(App):
    def on_mount(self) -> ComposeResult:
        def my_callback(value: None | bool) -> None:
            print(value)
            self.exit()

        self.push_screen(
            PasswordPromptDialog(),
            callback=my_callback,
        )


if __name__ == "__main__":
    app = PasswordPromptApp()
    app.run()
