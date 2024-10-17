from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Button, Footer, Header, Input, Static


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
    def compose(self) -> ComposeResult:
        """
        Lays out the main UI elemens plus a header and footer
        """
        yield Header()
        yield Form()
        yield Footer()


if __name__ == "__main__":
    app = AddressBookApp()
    app.run()
