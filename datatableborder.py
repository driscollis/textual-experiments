# datatableborder.py

from textual.app import App, ComposeResult
from textual.widgets import DataTable


class DataTableTest(App):
    def compose(self) -> ComposeResult:
        yield DataTable(id="playlist")

    def on_mount(self) -> None:
        data = [
            ("No Music Found", "", ""),
            ("Press CTRL+L to load music files", "", ""),
        ]
        table = self.query_one(DataTable)
        table.clear(columns=True)
        table.add_columns(*data[0])
        table.add_rows(data[1:])
        table.cursor_type = "row"
        table.styles.border = ("heavy", "green")
        table.border_title = "Playlist"


if __name__ == "__main__":
    app = DataTableTest()
    app.run()
