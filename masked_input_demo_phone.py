from textual.app import App, ComposeResult
from textual.widgets import Label, MaskedInput


class MaskedInputApp(App):
    # (1)!
    CSS = """
    MaskedInput.-valid {
        border: tall $success 60%;
    }
    MaskedInput.-valid:focus {
        border: tall $success;
    }
    MaskedInput {
        margin: 1 1;
    }
    Label {
        margin: 1 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("Enter a valid phone number.")
        yield MaskedInput(
            template="(999)-999-9999;0",
        )


if __name__ == "__main__":
    app = MaskedInputApp()
    app.run()
