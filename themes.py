# themes.py

from textual.app import App, ComposeResult
from textual.widgets import Button


class SimpleApp(App):

    def compose(self) -> ComposeResult:
        yield Button("Open Themes")

    def on_button_pressed(self) -> None:
        self.search_themes()


if __name__ == "__main__":
    app = SimpleApp()
    app.run()
