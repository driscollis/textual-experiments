from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Header, Footer, Input, Static


class TestApp(App):
    """
    A Textual App for modifying Jenkins jobs
    """

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Input(id="search_input")


if __name__ == "__main__":
    app = TestApp()
    app.run()
