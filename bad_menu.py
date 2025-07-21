import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="wx.Menu Tutorial")

        self.panel = wx.Panel(self, wx.ID_ANY)

        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        exit_menu_item = file_menu.Append(wx.NewId(), "Exit", "Exit the application")
        menu_bar.Append(file_menu, "&File")
        self.Bind(wx.EVT_MENU, self.on_exit, exit_menu_item)
        self.SetMenuBar(menu_bar)

    def on_exit(self, event):
        self.Close()


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame().Show()
    app.MainLoop()
