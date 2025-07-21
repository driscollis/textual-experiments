from textual.app import App, ComposeResult
from textual.widgets import Label, Button
from textual.containers import Horizontal


class Resizer(App):

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Label("", id="size_lbl"),
            Button("One"),
            Button("Two"),
            Button("Three"),
            Button("Four"),
        )


    def on_resize(self):
        self.query_one("#size_lbl").update(f"Size: {self.size.width} x {self.size.height}")

app = Resizer()
app.run()
