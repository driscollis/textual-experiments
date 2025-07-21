# progressbar_demo.py

from textual.app import App, ComposeResult
from textual.containers import Center, Middle
from textual.timer import Timer
from textual.widgets import Button, ProgressBar

class Progress(App[None]):
    timer = Timer

    def compose(self) -> ComposeResult:
        with Center():
            with Middle():
                yield ProgressBar()
                yield Button("Start")

    def on_mount(self) -> None:
        """
        Set up the timer to simulate progress
        """
        self.timer = self.set_interval(1 / 10, self.advance_progressbar, pause=True)

    def advance_progressbar(self) -> None:
        """
        Called to advance the progress bar
        """
        self.query_one(ProgressBar).advance(1)

    def on_button_pressed(self) -> None:
        """
        Event handler that is called when button is pressed
        """
        self.query_one(ProgressBar).update(total=100)
        self.timer.resume()

if __name__ == "__main__":
    app = Progress()
    app.run()
