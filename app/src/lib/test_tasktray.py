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
        """OverRide Method"""
        global menu
        menu = wx.Menu()
        self.createMenu()
        return menu

    def addSeparator(self) -> None:
        """タスクトレイの区切り線を挿入"""
        global menu
        menu.AppendSeparator()
    
    # -------------------------------------------------------------------------
    def createMenu(self) -> None:
        """ここでタスクトレイの内容(表示文字列とクリック時実行関数)を組み立てる"""
        self.addMenuItem('test', lambda e=self.__getEventOnClick: self.foo(e))
        self.addMenuItem('test2', lambda e=self.__getEventOnClick: self.bar(e))
        self.addSeparator()
        self.addMenuItem('exit', lambda e=self.__getEventOnClick: self.exit(e))

    def foo(self, e) -> None:
        print("foo")
    
    def bar(self, e) -> None:
        print("bar")
    
    def exit(self, e):
        wx.CallAfter(self.Destroy)
        self.frame.Close()
    # -------------------------------------------------------------------------

    def __getEventOnClick(self, event) -> object:
        """クリックイベントを取得する"""
        return event

    def addMenuItem(self, label, func):
        """メニューアイテムを追加するメソッド"""
        global menu
        item = wx.MenuItem(menu, -1, label)
        menu.Bind(wx.EVT_MENU, func, id=item.GetId())
        menu.Append(item)
        return item


class App(wx.App):
    tooltip = ""
    favicon_path = ""

    def OnInit(self):
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame, self.tooltip, self.favicon_path)
        return True
    
    def start(self) -> None:
        self.MainLoop()

class CreateTaskTray:
    def __init__(self, tooltip, favicon_path) -> None:
        App.tooltip = tooltip
        App.favicon_path = favicon_path
        app = App(False)
        self.app = app
    
    def start(self) -> None:
        self.app.start()

if __name__ == "__main__":
    TRAY_TOOLTIP = "FitScreenWindow"
    TRAY_ICON = r"C:\Users\tmgtmg\GoogleDrive\Project-FitScreenWindow\FitScreenWindow\app\images\favicon.ico"
    t = CreateTaskTray(TRAY_TOOLTIP, TRAY_ICON)
    t.start()
