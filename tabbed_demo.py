# tabbed_demo.py

from textual.app import App, ComposeResult
from textual.widgets import Button, Markdown, TabbedContent

PYTHON = """
# Python - An Amazing Language

You should use Python!

## Features

- Easy and readable
- Can run almost anywhere
- Python is fast enough
"""

C = """
# C++ - When You Want FAST

Fast but harder to learn than Python

## Features

- Stupid fast
- Harder to code
- Makes small exes
"""

RUBY = """
# Ruby - A Web Language

Expressive and versatile

## Features

- Has a popular web framework
- Interpretive
"""


class TabbedDemo(App):
    def compose(self) -> ComposeResult:
        self.close_button = Button("Close", id="close")

        tabs = ("Python", "C++", "Ruby")

        with TabbedContent(*tabs):
            yield Markdown(PYTHON)
            yield Markdown(C)
            yield Markdown(RUBY)

        yield self.close_button

    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"
        self.close_button.styles.background = "red"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.id)


if __name__ == "__main__":
    app = TabbedDemo()
    app.run()
