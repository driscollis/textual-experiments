import pathlib
from typing import Iterable

from rich.text import Text
from textual import on
from textual.app import ComposeResult
from textual.containers import Grid
from textual.message import Message
from textual.screen import Screen, ModalScreen
from textual.widgets import Button, DirectoryTree, Input, Label


class Filtered(DirectoryTree):
    def filter_paths(self, paths: Iterable[pathlib.Path]) -> Iterable[pathlib.Path]:
        return [path for path in paths if path.is_dir()]


class WarningScreen(Screen):
    """
    Creates a pop-up Screen that displays a warning message to the user
    """

    def __init__(
        self, warning_message: str = "ERROR: You need to specify something to change"
    ) -> None:
        super().__init__()
        self.warning_message = warning_message

    def compose(self) -> ComposeResult:
        """
        Create the UI in the Warning Screen
        """
        yield Grid(
            Label(self.warning_message, id="warning_msg"),
            Button("OK", variant="primary", id="ok_warning"),
            id="warning_dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Event handler for when the OK button - dismisses the screen
        """
        self.app.pop_screen()
        event.stop()


class NewFolderScreen(ModalScreen):
    CSS_PATH = "new_folder_screen.tcss"

    def __init__(self, current_directory: pathlib.Path) -> None:
        super().__init__()
        self.current_directory = current_directory

    def compose(self) -> ComposeResult:
        yield Input(placeholder="New Folder Name", id="new_folder")
        yield Button("OK", variant="primary", id="ok")
        yield Button("Cancel", id="cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        event.stop()
        if event.button.id == "cancel":
            self.dismiss()


class FolderBrowser(ModalScreen):
    class Selected(Message):
        """
        File selected message
        """

        def __init__(self, attr: str) -> None:
            self.attr = attr
            super().__init__()

    def __init__(self) -> None:
        super().__init__()
        self.selected_file = pathlib.Path("")

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Choose a directory:", id="choose_lbl"),
            Filtered("c:\\", id="filtered"),
            Label("Folder:", id="folder_lbl"),
            Input(id="folder_path_input"),
            Button("New Folder", id="create_folder"),
            Button(
                f"{Text.from_markup(':heavy_check_mark:')}  OK",
                variant="primary",
                id="select_folder",
            ),
            Button(f"{Text.from_markup(":cross_mark:")}  Cancel", id="cancel"),
            id="folder_browser",
        )
        # yield Label("Choose a directory:")
        # yield Filtered("c:\\")

        # with Horizontal(id="folder_name"):
        # yield Label("Folder:")
        # yield Input()

        # with Horizontal(id="bottom_row"):
        # yield Button("Make New Folder", id="create_folder")
        # yield Button("Select Folder", variant="primary", id="select_folder")
        # yield Button("Cancel", id="cancel")

    @on(DirectoryTree.DirectorySelected)
    def on_file_selected(self, event: DirectoryTree.DirectorySelected) -> None:
        """
        Called when the FileSelected Message is emitted from the DirectoryTree
        """
        self.selected_file = event.path
        self.log.info(f"FILE SELECTED IN FILEBROWSER: {self.selected_file}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Event handler for when the load file button is pressed
        """
        event.stop()
        if event.button.id == "cancel":
            self.dismiss()
        elif event.button.id == "select_folder":
            self.post_message(self.Selected(f"{self.selected_file}"))
        elif event.button.id == "create_folder":
            self.app.push_screen(NewFolderScreen(self.selected_file))
