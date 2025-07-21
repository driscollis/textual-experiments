from textual.app import App, ComposeResult
from textual.widgets import Label


class TestApp(App):
    CSS_PATH = "alignment.tcss"

    def compose(self) -> ComposeResult:
        yield Label("0", id="solution")

if __name__ == "__main__":
    app = TestApp()
    app.run()
