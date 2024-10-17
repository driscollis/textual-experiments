# listview_demo.py

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, ListItem, ListView, TextArea


class ListViewDemo(App):
    def __init__(self) -> None:
        super().__init__()
        self.current_selection = None

    def compose(self) -> ComposeResult:
        text_area = TextArea()
        self.title = "Change Theme"
        themes = list(text_area.available_themes)
        themes.sort()
        theme_items = [ListItem(Label(theme)) for theme in themes]
        yield ListView(*theme_items, id="themes")

    @on(ListView.Highlighted)
    @on(ListView.Selected)
    def on_item(self, event) -> None:
        self.current_selection = str(event.item.query_one(Label).renderable)
        self.notify(f"You selected {self.current_selection}")


if __name__ == "__main__":
    app = ListViewDemo()
    app.run()
