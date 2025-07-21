from textual.app import App, ComposeResult
from textual.widgets import Placeholder


class Resizer(App):

    def compose(self) -> ComposeResult:
        yield Placeholder()

app = Resizer()
app.run()
