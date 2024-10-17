from textual.app import App, ComposeResult

from textual_plotext import PlotextPlot


class BarApp(App[None]):
    def compose(self) -> ComposeResult:
        yield PlotextPlot()

    def on_mount(self) -> None:
        plt = self.query_one(PlotextPlot).plt

        languages = ["Python", "PHP", "Ruby", "C++", "Java"]
        percentages = [36, 10, 25, 10, 19]

        plt.theme("textual-sahara")
        plt.bar(languages, percentages)
        plt.title("Popular Programming Languages")


if __name__ == "__main__":
    BarApp().run()
