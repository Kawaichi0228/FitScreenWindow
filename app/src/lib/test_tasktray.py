import os

import wx
import wx.adv


class TaskBarIcon(wx.adv.TaskBarIcon):

    def __init__(self, frame, tooltip, favicon_path):
        self.tooltip = tooltip

        if not self.__isExistsFavicon(favicon_path):
            raise FileNotFoundError("指定されたパスのアイコンが見つかりません")
        self.favicon_path = favicon_path

        self.frame = frame
        super(TaskBarIcon, self).__init__()

        self.__setFavicon(self.favicon_path)

        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.__bindFunction)

    def __isExistsFavicon(self, favicon_path) -> bool:
        return os.path.exists(favicon_path)

    def __setFavicon(self, path):
        icon = wx.Icon(wx.Bitmap(path))
        self.SetIcon(icon, self.tooltip)

    def __bindFunction(self) -> None: ...

    def CreatePopupMenu(self):
        global menu
        menu = wx.Menu()
        self.createMenu()
        return menu

    def addSeparator(self) -> None:
        """タスクトレイの区切り線を挿入"""
        global menu
        menu.AppendSeparator()

    def createMenu(self) -> None:
        self.createMenuItem('test', self.on_open_site)
        self.addSeparator()
        self.createMenuItem('exit', self.on_exit)

    def on_open_site(self, event):
        print("aaa")
    
    def on_exit(self, event):
        wx.CallAfter(self.Destroy)
        self.frame.Close()

    def createMenuItem(self, label, func):
        """メニューアイテムを追加するメソッド"""
        global menu
        item = wx.MenuItem(menu, -1, label)
        menu.Bind(wx.EVT_MENU, func, id=item.GetId())
        menu.Append(item)
        return item


class App(wx.App):

    def OnInit(self):
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        TRAY_TOOLTIP = "FitScreenWindow"
        TRAY_ICON = r"C:\Users\tmgtmg\GoogleDrive\Project-FitScreenWindow\FitScreenWindow\app\images\favicon.ico"
        TaskBarIcon(frame, TRAY_TOOLTIP, TRAY_ICON)
        return True


if __name__ == "__main__":
    app = App(False)
    app.MainLoop()