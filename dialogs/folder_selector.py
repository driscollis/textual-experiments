import pathlib

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Center
from textual.widgets import Button, Input, DirectoryTree, Footer, Label


from screens import FolderBrowser


class FolderSelectorApp(App):
    CSS_PATH = "folder.tcss"
    BINDINGS = [
        ("ctrl+o", "open", "Choose Folder"),
        ("escape", "esc", "Exit dialog"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.app_selected_file = pathlib.Path("")

    def compose(self) -> ComposeResult:
        yield Input()
        with Center():
            yield Button("Quit", variant="primary", id="quit_button")
        yield Footer()

    # Event handlers
    @on(DirectoryTree.FileSelected)
    def on_file_browser_selection(self, event: DirectoryTree.FileSelected) -> None:
        self.app_selected_file = event.path

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit()

    def on_folder_browser_selected(self, message: FolderBrowser.Selected) -> None:
        """
        Message handler - Called when a custom message is posted from FileBrowser
        """
        self.app.pop_screen()

        folder = self.query_one(Input)
        folder.value = f"You chose: {message.attr}"

    # Keyboard shortcut handlers
    def action_open(self) -> None:
        self.push_screen(FolderBrowser())

    def action_esc(self) -> None:
        """
        Exit a screen but not the application itself
        """
        try:
            self.app.pop_screen()
        except:
            pass


if __name__ == "__main__":
    app = FolderSelectorApp()
    app.run()
