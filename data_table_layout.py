import datetime

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, DataTable, Header, Label

class MyApp(App):

    CSS_PATH = "myapp.tcss"

    def compose(self) -> ComposeResult:
        """
        Create the user interface
        """
        now =  datetime.datetime.now().isoformat()
        self.last_updated = Label(f"Last Updated: {now[0:-7]}",
                                  id="last_updated",
                                  )

        yield Header()
        yield Vertical(
                    DataTable(id="datatable"),
                    Horizontal(
                        Button("OK", variant="primary", id="ok"),
                        Button("Cancel", variant="error", id="cancel"),
                        self.last_updated,
                        id="button_row",
                    ),
                    id="main_tab",
                )

    def on_mount(self) -> None:
        rows = [("Name", "Occupation", "Country",),
                ("Mike", "Python Wrangler", "USA",),
                ("Bill", "Engineer", "UK",),
                ("Dee", "Manager", "Germany"),
                ]
        table = self.query_one(DataTable)
        table.clear(columns=True)
        table.add_columns(*rows[0])
        table.add_rows(rows[1:])


if __name__ == "__main__":
    app = MyApp()
    app.run()