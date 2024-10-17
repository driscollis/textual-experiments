from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Placeholder


class KeylineDemoApp(App):
    CSS_PATH = "keyline_horizontal.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Placeholder()
            yield Placeholder()
            yield Placeholder()


if __name__ == "__main__":
    app = KeylineDemoApp()
    app.run()
