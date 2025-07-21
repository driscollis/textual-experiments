import random
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Static

class BindingUpdateApp(App):

    BINDINGS = [
        Binding(key="u", action="update_keymap", description="Update Keymap", id="app.update"),
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
        yield Static("Keymap updater", id="keymap_label")

    def action_update_keymap(self) -> None:
        self.set_keymap({"app.background": "f5,ctrl+a"})
        self.notify("Updated keymap")

    def action_change_background(self) -> None:
        self.screen.styles.background = random.choice(self.COLORS)

if __name__ == "__main__":
    app = BindingUpdateApp()
    app.run()


