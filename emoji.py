# emoji.py

from rich.text import Text
from textual.app import App, ComposeResult
from textual.widgets import Label


class SimpleApp(App):
    # https://github.com/Textualize/rich/blob/master/rich/_emoji_codes.py

    def compose(self) -> ComposeResult:
        magnifier = Text.from_markup(":magnifying_glass_tilted_right:")
        floppy = Text.from_markup(":floppy_disk:")
        folder = Text.from_markup(":open_file_folder:")
        warning = Text.from_markup(":warning:")
        info = Text.from_markup(":information:")
        question = Text.from_markup(":question_mark:")
        exclamation = Text.from_markup(":exclamation:")
        yield Label(floppy)


if __name__ == "__main__":
    app = SimpleApp()
    app.run()
