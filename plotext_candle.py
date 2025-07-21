import yfinance as yf

from textual.app import App, ComposeResult
from textual_plotext import PlotextPlot

class ScatterApp(App[None]):

    def compose(self) -> ComposeResult:
        yield PlotextPlot()

    def on_mount(self) -> None:
        plt = self.query_one(PlotextPlot).plt
        plt.date_form('d/m/Y')
        start = plt.string_to_datetime('02/01/2025')
        end = plt.today_datetime()

        data = yf.download('goog', start, end)
        dates = plt.datetimes_to_string(data.index)
        plt.candlestick(dates, data)

        plt.title("Google Stock Price CandleSticks")
        plt.xlabel("Date")
        plt.ylabel("Stock Price $")

if __name__ == "__main__":
    ScatterApp().run()