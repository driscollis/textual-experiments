# long_running_process.py

import asyncio

from textual import on, work
from textual.app import App, ComposeResult
from textual.widgets import Button, Label


class MyApp(App):
    def compose(self) -> ComposeResult:
        self.run_button = Button("Run", variant="success", id="run")
        self.text = Label("Not Running!")
        yield self.run_button
        yield self.text

    @on(Button.Pressed, "#run")
    def name_me_something_descriptive(self, even: Button.Pressed) -> None:
        # Call the long running process here
        self.long_running_process()

    @work
    async def long_running_process(self):
        self.query_one("#run").disabled = True
        self.text.update("Running!!!")
        await asyncio.sleep(5)
        self.text.update("Finished processing!")
        self.query_one("#run").disabled = False


if __name__ == "__main__":
    app = MyApp()
    app.run()
