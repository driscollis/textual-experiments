from textual.app import App, ComposeResult

from textual_plotext import PlotextPlot

class BarChartApp(App[None]):

    def compose(self) -> ComposeResult:
        yield PlotextPlot()

    def on_mount(self) -> None:
        languages = ["Python", "C++", "PHP", "Ruby", "Julia", "COBOL"]
        percentages = [14, 36, 11, 8, 7, 4]
        plt = self.query_one(PlotextPlot).plt
        y = plt.bar(languages, percentages)
        plt.scatter(y)
        plt.title("Programming Languages") # to apply a title

if __name__ == "__main__":
    BarChartApp().run()
