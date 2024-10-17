from textual.app import App, ComposeResult
from textual.containers import Center
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Footer, Header, Input, Static, Label


class QuitScreen(ModalScreen):
    """Screen with a dialog to quit."""

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to quit?", id="question"),
            Button("Quit", variant="error", id="quit"),
            Button("Cancel", variant="primary", id="cancel"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()
        else:
            self.app.pop_screen()


class Form(Static):
    def compose(self) -> ComposeResult:
        """
        Creates the main UI elements
        """
        yield Input(id="first_name", placeholder="First Name")
        yield Input(id="last_name", placeholder="Last Name")
        yield Input(id="address", placeholder="Address")
        yield Input(id="city", placeholder="City")
        yield Input(id="state", placeholder="State")
        yield Input(id="zip_code", placeholder="Zip Code")
        yield Input(id="email", placeholder="email")
        with Center():
            yield Button("Save", id="save_button")


class AddressBookApp(App):
    CSS_PATH = "modal.tcss"
    BINDINGS = [("q", "request_quit", "Quit")]

    def compose(self) -> ComposeResult:
        """
        Lays out the main UI elemens plus a header and footer
        """
        yield Header()
        yield Form()
        yield Footer()

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""
        self.push_screen(QuitScreen())


if __name__ == "__main__":
    app = AddressBookApp()
    app.run()
