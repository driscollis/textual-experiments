from textual.app import App, ComposeResult
from textual.containers import Center
from textual.message import Message
from textual.screen import Screen
from textual.widgets import Button, DataTable, DirectoryTree


class FileBrowser(Screen):
    class Selected(Message):
        """
        File selected message
        """

        def __init__(self, attr: str) -> None:
            self.attr = attr
            super().__init__()

    def compose(self) -> ComposeResult:
        yield DirectoryTree("./")
        yield Button("Load File", variant="primary", id="load_file")

    def on_button_pressed(self) -> None:
        self.log.info("Screen button pressed")
        self.post_message(self.Selected("selected"))


class Test(App):
    def compose(self) -> ComposeResult:
        yield DataTable()
        with Center():
            yield Button(f"Remote", variant="primary", id="remote_button")

    def on_mount(self) -> None:
        self.push_screen(FileBrowser())

    def on_file_browser_selected(self, message: FileBrowser.Selected) -> None:
        self.log.info("IN on_file_browse() method")
        self.app.pop_screen()


if __name__ == "__main__":
    app = Test()
    app.run()
