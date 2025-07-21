# toggle.py

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button


class ToggleButtonApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Button("Toggle", id="toggle")

    @on(Button.Pressed, "#toggle")
    def toggle(self, event: Button.Pressed) -> None:
        button = event.button
        if str(button.label) == "Toggle":
            button.label = "UnToggle!!!"
        else:
            button.label = "Toggle"



if __name__ == "__main__":
    ToggleButtonApp().run()
