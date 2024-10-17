
from textual.app import App, ComposeResult
from textual.widgets import MarkdownViewer


class MarkdownViewerApp(App):
    def compose(self) -> ComposeResult:
        with open(r"README.md", encoding="utf-8") as file:
            md = file.read()

        yield MarkdownViewer(md, show_table_of_contents=True)


if __name__ == "__main__":
    app = MarkdownViewerApp()
    app.run()