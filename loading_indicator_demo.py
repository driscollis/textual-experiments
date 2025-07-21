import time
from textual.app import App, ComposeResult
from textual.containers import Center, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Label, LoadingIndicator
from textual import work


class Loading(ModalScreen):
    DEFAULT_CSS = """
    Loading {
        align: center middle;
        background: $primary 30%;
    }

    #loading_container {
        width: 50%;
        height: 50%;
        align: center middle;
    }

    #loading_message {
        background: blue 50%;
        border: wide white;
        width: auto;
    }
    """

    def __init__(self, message: str) -> None:
        super().__init__()
        self.message = message

    def compose(self) -> ComposeResult:
        yield Vertical(
            Label(self.message, id="loading_message"),
            LoadingIndicator(id="loading_indicator"),
            id="loading_container"
        )


class TestLoadingIndicator(App):

    def compose(self) -> ComposeResult:
        yield Button("Show Loading Indicator")

    def on_button_pressed(self) -> None:
        self.long_running_process()
        self.push_screen(Loading("Running long process"))

    @work(exclusive=True, thread=True)
    def long_running_process(self) -> None:
        time.sleep(5)
        self.pop_screen()

if __name__ == "__main__":
    app = TestLoadingIndicator()
    app.run()
