
from textual.app import App, ComposeResult
from textual.widgets import Button


class WelcomeButton(App):

    def compose(self) -> ComposeResult:
        yield Button("Exit")

    def on_button_pressed(self) -> None:
        self.mount(Button("Other"))
        self.notify("You pressed the button!", title="Info Message", severity="error")


if __name__ == "__main__":
    app = WelcomeButton()
    app.run()
