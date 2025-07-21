# simple_color_picker.py

from textual import on
from textual._color_constants import ANSI_COLORS, COLOR_NAME_TO_RGB
from textual.app import App, ComposeResult
from textual.containers import Center, Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Header, Select, Placeholder

class SimpleColorPickerDialog(ModalScreen):

    #CSS_PATH = "color_picker.tcss"

    DEFAULT_CSS = """
    SimpleColorPickerDialog {
        align: center middle;
        background: $primary 30%;

        #simple-color-dlg {
            width: 85;
            height: 18;
            border: thick $background 70%;
            content-align: center middle;
            margin: 1;
        }

        Button {
            width: 50%;
            margin: 1;
        }

        Placeholder {
                    width: 100%;
                    height:5;
                    margin: 1
            }
    }
    """

    def compose(self):
        colors = ANSI_COLORS + list(COLOR_NAME_TO_RGB.keys())
        colors.sort()
        yield Vertical(
            Header(),
            Center(Select.from_values(colors, id="simple-color-picker")),
            Center(Placeholder(id="chosen-color")),
            Center(
                Horizontal(
                     Button("OK", variant="primary", id="simple-color-ok"),
                     Button("Cancel", variant="error", id="simple-color-cancel"),
                )
            ),
            id="simple-color-dlg",
        )


class SimpleColorPickerApp(App):
    def on_mount(self) -> ComposeResult:
        def my_callback(value: None | bool) -> None:
            print(value)
            self.exit()

        self.push_screen(
            SimpleColorPickerDialog(),
            callback=my_callback,
        )


if __name__ == "__main__":
    app = SimpleColorPickerApp()
    app.run()
