from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, DataTable, Footer

class Test(App):

    CSS_PATH = "datatable_test.tcss"

    def compose(self) -> ComposeResult:
        """
        Create the user interface
        """
        yield Vertical(
            DataTable(id="datatable"),

            Horizontal(
                Button("Remote Desktop", variant="primary", id="remote_button"),
                Button("Report Issue", variant="error", id="report_button"),
                id="button-row"
            ),
            id="main_tab"
        )
        yield Footer()

    def on_mount(self) -> None:
        ROWS = [("No Data Found", "", ""), ("Press CTRL+L to load CSV file", "", "")]
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

app = Test()
app.run()
