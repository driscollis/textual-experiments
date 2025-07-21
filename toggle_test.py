from textual.app import App, ComposeResult
from textual.widgets import Button

class ToggleButton(Button):

<<<<<<< Updated upstream
    def __init__(self, initial_label: str, toggled_label: str, border: tuple[str, str]=("double", "gold"), variant="default", *, name=None, id=None, classes=None, disabled=False, tooltip=None, action=None):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self.toggled = False
        self.label = initial_label
        self.initial_label = initial_label
        self.toggled_label = toggled_label
=======
    def __init__(self, labels: dict[int, str],
                 default_label: str,
                 border: tuple[str, str]=("double", "gold"),
                 variant="default", *,
                 name=None, id=None, classes=None, disabled=False,
                 tooltip=None, action=None):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self.toggled = False
        self.label = default_label
        self.labels = labels
>>>>>>> Stashed changes
        self.border = border
        self.variant = variant

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if not self.toggled:
            event.button.styles.border = self.border
        else:
            event.button.styles.border = None

        self.toggled = not self.toggled
        event.button.label = self.toggled_label if self.toggled else self.initial_label



class TestToggle(App):

    def compose(self) -> ComposeResult:
        yield ToggleButton(initial_label="On", toggled_label="Off")

    def on_button_pressed(self, event: ToggleButton.Pressed):
        if event.button.toggled:
            event.button.styles.background = "blue"
        else:
            event.button.styles.background = "red"


if __name__ == "__main__":
    app = TestToggle()
    app.run()
