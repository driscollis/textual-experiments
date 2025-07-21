from pathlib import Path
from typing import Iterable

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import DirectoryTree


class Filtered(DirectoryTree):
    def filter_paths(self, paths: Iterable[Path]) -> Iterable[Path]:
        return [path for path in paths if path.is_dir()]


class FolderBrowser(App):
    def compose(self) -> ComposeResult:
        yield Filtered("/")

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
