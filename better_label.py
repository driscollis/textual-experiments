from textual.app import App, ComposeResult
from textual.widgets import Label, Button

class BetterLabel(Label):

    def __init__(self, renderable="", *, variant=None, expand=False, shrink=False, markup=True, name=None, id=None, classes=None, disabled=False):
        super().__init__(
            renderable,
            expand=expand,
            shrink=shrink,
            markup=markup,
            name=name,
            id=id,
            classes=classes,
            disabled=disabled,
        )
        self.text = renderable

    def update(self, content=""):
        super().update(content=content)
        self.text = content


class LabelApp(App):

    def compose(self) -> ComposeResult:
        yield BetterLabel("Initial")
        yield Button("Check Label")

    def on_button_pressed(self, event: Button.Pressed):
        lbl =  self.query_one(BetterLabel, BetterLabel)
        self.notify(f"Label text: {lbl.text = }")
        text = "Initial" if lbl.text != "Initial" else "Other"
        lbl.update(text)



if __name__ == "__main__":
    app = LabelApp()
    app.run()
