import uuid

from textual.app import App, ComposeResult
from textual.widgets import Button, DataTable, Footer, TabbedContent, TabPane

class NewTab(TabPane):

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        ROWS = [("No Data Found", "", ""), ("Press CTRL+L to load CSV file", "", "")]
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])

class TabbedApp(App):

    def compose(self) -> ComposeResult:
        yield Footer()
        with TabbedContent(initial="nada"):
            with TabPane("Nada", id="nada"): # tab one
                yield Button("New Tab")

    def on_button_pressed(self) -> None:
        tab_mgr = self.query_one(TabbedContent)
        tab_id = f"tab_{uuid.uuid4()}"
        new_tab = NewTab("New Tab", id=tab_id)
        tab_mgr.add_pane(new_tab)
        tab_mgr.active = tab_id


if __name__ == "__main__":
    app = TabbedApp()
    app.run()
