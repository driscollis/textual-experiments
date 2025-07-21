from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Label


class SimpleListView(ListView):
    def compose(self) -> ComposeResult:
        for i in range(1, 11):
            yield ListItem(Label(f"List Item {i}"))


class SimpleApp(App):
    CSS = """
    ListItem.-highlight {
        background: red;  /* Set the background color for highlighted items */
        color: white;     /* Set the text color for highlighted items */
    }
    """

    def compose(self) -> ComposeResult:
        yield SimpleListView()


if __name__ == "__main__":
    app = SimpleApp()
    app.run()
