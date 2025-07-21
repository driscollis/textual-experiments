from textual import on
from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree


class FolderBrowser(App):
    def compose(self) -> ComposeResult:
        yield DirectoryTree("/")

    @on(DirectoryTree.FileSelected)
    def on_file_selected(self, event: DirectoryTree.FileSelected) -> None:
        """
        Called when the FileSelected Message is emitted from the DirectoryTree
        """
        selected_file = event.path
        self.log.info(f"FILE SELECTED IN FILEBROWSER: {selected_file}")


if __name__ == "__main__":
    app = FolderBrowser()
    app.run()
