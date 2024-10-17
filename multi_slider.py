# https://gist.github.com/willmcgugan/efd05c26b49174ca65652264b425cbaa

from textual.app import App, ComposeResult
from textual.widgets import Footer, Label
from textual.widget import Widget


class SideBar(Widget):
    def compose(self) -> None:
        yield Label("Sidebar")


class TopBar(Widget):
    def compose(self) -> None:
        yield Label("Topbar")


class SlideApp(App):
    BINDINGS = [
        ("s", "toggle_sidebar", "Show Sidebar"),
        ("t", "toggle_topbar", "Show Topbar"),
    ]

    CSS = """
    SideBar {
        width: 24;
        dock: left;
        height: 100%;
        background: $panel;
        border: tall red;
        offset-x: -100%;
        transition: offset 300ms in_out_cubic;
    }
    SideBar.visible {
        offset-x: 0;
    }
    TopBar {
        dock: top;
        width: 100%;
        height: 5;
        border: solid green;
        offset-y: -100%;
        transition: offset 300ms in_out_cubic;
    }
    TopBar.visible {
        offset-y: 0;
    }
    """

    def compose(self) -> ComposeResult:
        yield Footer()
        yield SideBar()
        yield TopBar()

    def action_toggle_sidebar(self) -> None:
        self.query_one(SideBar).toggle_class("visible")

    def action_toggle_topbar(self) -> None:
        self.query_one(TopBar).toggle_class("visible")


app = SlideApp()
app.run()
