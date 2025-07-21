# tree_experiments.py

from rich.text import Text
from textual.app import App, ComposeResult
from textual.widgets import Tree

class TreeApp(App):

    def compose(self) -> ComposeResult:
        self.top_level_nodes: dict[str, int] = {}
        nodes = {}
        leaves = ["one", "two", "three"]

        tree = Tree("root")
        tree.root.expand()

        some_file_tests = tree.root.add(Text("some_file.py", style="green"))
        self.top_level_nodes["some_file.py"] = some_file_tests.id
        leaf_nodes = {}
        for leaf in leaves:
            leaf_obj = some_file_tests.add_leaf(leaf)
            leaf_nodes[leaf] = leaf_obj.id
        nodes["some_file.py"] = leaf_nodes

        some_more_tests = tree.root.add(Text("another_file.py", style="red"))
        self.top_level_nodes["another_file.py"] = some_more_tests.id
        leaf_nodes = {}
        for leaf in leaves:
            leaf_obj = some_more_tests.add_leaf(leaf)
            leaf_nodes[leaf] = leaf_obj.id
        nodes["another_file.py"] = leaf_nodes
        print(f"{self.top_level_nodes = }  {nodes = }")
        yield tree


if __name__ == "__main__":
    app = TreeApp()
    app.run()