# button_which_pressed.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class QueryApp(App):

    def compose(self) -> ComposeResult:
        yield Label("Press a button", id="label")
        yield Button("One", id="one")
        yield Button("Two", id="two")
        yield Button("Three")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.notify(event.button.label)

if __name__ == "__main__":
    app = QueryApp()
    app.run()
