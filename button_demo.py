from textual.app import App, ComposeResult
from textual.widgets import Label, Button


class BeatleApp(App[str]):
    def compose(self) -> ComposeResult:
        yield Label("Are you the Walrus?")
        yield Button("Yes!", id="yes", variant="primary")
        yield Button("No", id="no", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


if __name__ == "__main__":
    app = BeatleApp()
    answer = app.run()
    print(answer)
