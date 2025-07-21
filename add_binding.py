import random
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Static

class NewBinding(App):

    BINDINGS = [
        Binding(key="u", action="add_binding", description="Update Keymap", id="app.add_binding"),
        Binding(key="ctrl+a", action="change_background", description="Change Background", id="app.background"),
    ]

    COLORS = [
            "white",
            "maroon",
            "red",
            "purple",
            "fuchsia",
            "olive",
            "yellow",
            "navy",
            "teal",
            "aqua",
        ]

    def compose(self) -> ComposeResult:
        yield Static("Add new binding", id="binder")

    def action_add_binding(self) -> None:
        self.bind("f5", "change_background")
        self.notify("Added F5 binding")

    def action_change_background(self) -> None:
        self.screen.styles.background = random.choice(self.COLORS)

if __name__ == "__main__":
    app = NewBinding()
    app.run()


