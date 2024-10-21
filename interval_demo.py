# interval_demo.py

import datetime
import time

from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class SimpleApp(App):

    def __init__(self) -> None:
        super().__init__()
        self.start_time = 0

    def compose(self) -> ComposeResult:
        yield Label("Timer not started")
        yield Button("Start Interval Timer")

    def on_button_pressed(self) -> None:
        self.log.info("Starting interval")
        self.set_interval(5, self.update_label)

    def update_label(self) -> None:
        label = self.query_one(Label)
        value = datetime.datetime.fromtimestamp(time.time())
        label.update(f"Updated at {value:%H:%M:%S}")
        self.log.info(f"Updated at {value:%H:%M:%S}")


if __name__ == "__main__":
    app = SimpleApp()
    app.run()
