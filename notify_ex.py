# notify_ex.py

from textual.app import App, ComposeResult
from textual.widgets import Button


class WelcomeButton(App):
    def compose(self) -> ComposeResult:
        yield Button("Exit")
        self.notify("It's a trap!", severity="error", timeout=10)

    def on_button_pressed(self) -> None:
        self.notify("Exiting!", severity="information", timeout=10)


if __name__ == "__main__":
    app = WelcomeButton()
    app.run()
