from textual.app import App
from textual_pandas.widgets import DataFrameTable
import pandas as pd

# Pandas DataFrame
df = pd.DataFrame()
df["Name"] = ["Dan", "Ben", "Don", "John", "Jim", "Harry"]
df["Score"] = [77, 56, 90, 99, 83, 69]
df["Grade"] = ["C", "F", "A", "A", "B", "D"]


class PandasApp(App):
    def compose(self):
        yield DataFrameTable()

    def on_mount(self):
        table = self.query_one(DataFrameTable)
        table.add_df(df)


if __name__ == "__main__":
    app = PandasApp()
    app.run()
