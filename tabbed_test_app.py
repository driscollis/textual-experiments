from textual.app import App, ComposeResult
from textual.widgets import Button, Label, TabbedContent, TabPane, Tree

class NewPane(TabPane):

    def compose(self) -> ComposeResult:
        tree: Tree[str] = Tree("Tables")
        tree.root.expand()
        table_names = ["Rock", "Paper", "Scissors"]
        for table_name in table_names:
            table = tree.root.add(table_name)
        yield tree

class ExampleApp(App):

    def compose(self) -> ComposeResult:
        yield Button("Update", id="update")
        with TabbedContent("Database", id="tabbed_ui"):
            with TabPane("Database Structure"):
                yield Label("No data loaded")
            with TabPane("Table Viewer"):
                yield Label("No data loaded")
            with TabPane("Execute SQL"):
                yield Label("No data loaded")


    async def on_button_pressed(self) -> None:
        tabbed_content = self.query_one("#tabbed_ui", TabbedContent)
        await tabbed_content.clear_panes()
        await tabbed_content.add_pane(NewPane("Database Structure", id="data"))
        tabbed_content.active = "data"

if __name__ == "__main__":
    app = ExampleApp()
    app.run()