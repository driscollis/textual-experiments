import csv
import io
import subprocess

import pandas as pd
import openpyxl

from textual import on
from textual.app import App, ComposeResult
from textual.containers import Center
from textual.message import Message
from textual.screen import Screen
from textual.widgets import Button, DataTable, DirectoryTree

ROWS = [
    ("Pokemon Name", "PC Name", "Purpose", "App Team"),
    ("Bulbasaur", "WDX3GL0N83", "Mono", "Core"),
    ("Charizard", "WDX8KF5KQ3", "Stereo", "Core"),
    ("Charmander", "WDXMXL01723QL", "Stereo", "Core"),
    ("Chikorita", "WDX9JHQFT30", "Mono", "Core"),
    ("Cyndaquil", "WDXDPLQFT3", "Stereo", "Core"),
    ("Rhyhorn", "WDXBGHQFT3", "Nitro Mono", "Core"),
    ("Sceptile", "WDX6MF5KQ3", "Nitro Stereo", "Mono"),
    ("Treecko", "WDX2HHQFT30", "Nitro Stereo", "Core"),
    ("Venusaur", "WDXCJF5KQ3", "Stereo", "Mono"),
]


class FileBrowser(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.selected_file = ""

    def compose(self) -> ComposeResult:
        yield DirectoryTree("./")
        yield Button("Load File", variant="primary", id="load_file")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.log.info("In FileBrowser on_button_pressed()")
        event.stop()
        self.app.pop_screen()


class Test(App):
    def compose(self) -> ComposeResult:
        with Center():
            yield Button(f"Remote Desktop", variant="primary", id="remote_button")

    def on_mount(self) -> None:
        self.push_screen(FileBrowser())

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.log.info(f"In the app on_button_pressed() method")
        button = self.query_one(Button)
        if button.id == "load_file":
            return

        if self.selected_row is None:
            return


if __name__ == "__main__":
    app = Test()
    app.run()
