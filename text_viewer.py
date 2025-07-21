from argparse import ArgumentParser, Namespace

from textual.app import App, ComposeResult
from textual.widgets import Static


class TextViewerApp(App[None]):
    def __init__(self, cli_args: Namespace) -> None:
        super().__init__()
        self.args = cli_args
        try:
            with open(self.args.filepath) as fh:
                self.data = fh.read()
        except:
            self.data = "File not found"

    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"
        self.text_viewer.update(self.data)

    def compose(self) -> ComposeResult:
        self.text_viewer = Static()
        yield self.text_viewer


def get_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("filepath")
    return parser.parse_args()


def run() -> None:
    TextViewerApp(get_args()).run()


if __name__ == "__main__":
    run()
