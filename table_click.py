# table_click.py

import db_utility

from pathlib import Path
from textual import on
from textual.app import App, ComposeResult
from textual.events import Click
from textual.widgets import DataTable, Select


class TableViewerPane(App):

    def __init__(self, db_path: Path, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db_path = db_path
        self.tables = db_utility.get_table_names(self.db_path)
        print("TABLES")
        print(self.tables)
        self.tables.sort()
        self.selected_row_key = None
        self.columns = None
        self.last_column_key = None
        self.reverse = False

    def compose(self) -> ComposeResult:
        yield Select.from_values(self.tables, id="table_names_select", value=self.tables[0])
        yield DataTable(id="sqlite_table_data")

    def on_mount(self) -> None:
        self.update_sqlite_table_view()

    @on(Select.Changed, "#table_names_select")
    def update_sqlite_table_view(self) -> None:
        current_table = self.app.query_one("#table_names_select").value

        try:
            data = db_utility.get_data_from_table(self.db_path, current_table)
        except sqlite3.OperationalError:
            return

        self.columns = data[0]
        table = self.query_one(DataTable)
        table.clear(columns=True)
        table.add_columns(*self.columns)
        if len(data[1:]):
            table.add_rows(data[1:])
        else:
            table.add_rows([tuple(["" for x in data[0]])])

        table.cursor_type = "row"

    @on(DataTable.HeaderSelected, "#sqlite_table_data")
    def on_header_selected(self, event) -> None:

        table = self.query_one(DataTable)

        if self.last_column_key == event.column_key:
            self.reverse = not self.reverse
            table.sort(event.column_key, reverse=self.reverse)
        else:
            table.sort(event.column_key, reverse=False)
        self.last_column_key = event.column_key



TableViewerPane(r"C:\books\creating_tuis\code\examples\Chinook_Sqlite.sqlite").run()