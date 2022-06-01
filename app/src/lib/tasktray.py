# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import os
import wx
import wx.adv

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class TaskTray(wx.adv.TaskBarIcon):
    def __init__(self, frame, tooltip, favicon_path, item_list):
        self.tooltip = tooltip

        if not self.__isExistsFavicon(favicon_path):
            raise FileNotFoundError("指定されたパスのアイコンが見つかりません")
        self.favicon_path = favicon_path

        self.frame = frame
        super(TaskTray, self).__init__()

        self.item_list = item_list

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
        for item in self.item_list:
            self.__getMenuItem(item[0], lambda e=self.__getEventOnClick, func=item[1]: self.__bindFunction(e, func))

    def stopThread(self):
        wx.CallAfter(self.Destroy)
        self.frame.Close()
    # -------------------------------------------------------------------------

    def __bindFunction(self, e, func) -> None:
        func()

    def __getEventOnClick(self, event) -> object:
        """クリックイベントを取得する"""
        return event

    def __getMenuItem(self, label, func) -> object:
        """メニューアイテムを追加するメソッド"""
        global menu
        item = wx.MenuItem(menu, -1, label)
        menu.Bind(wx.EVT_MENU, func, id=item.GetId())
        menu.Append(item)
        return item


class TaskApp(wx.App):
    tooltip = ""
    favicon_path = ""

    def OnInit(self):
        frame=wx.Frame(None)
        self.frame = frame
        self.SetTopWindow(frame)
        return True
    
    def setTaskBarIcon(self, item_list) -> None:
        self.taskbar_icon = TaskTray(self.frame, self.tooltip, self.favicon_path, item_list)

    def stop(self) -> None:
        self.taskbar_icon.stopThread()
    
    def start(self) -> None:
        self.MainLoop()


class TaskMenuItem:
    def __init__(self) -> None:
        self.item_list = []

    def add(self, value, func) -> None:
        item = (value, func)
        self.item_list.append(item)

    def get(self) -> list:
        return self.item_list


class CreateTaskTray:
    def __init__(self, tooltip, favicon_path, item_list) -> None:
        TaskApp.tooltip = tooltip
        TaskApp.favicon_path = favicon_path
        app = TaskApp(False)
        app.setTaskBarIcon(item_list)
        self.app = app
    
    def startThread(self) -> None:
        self.app.start()

    def stopThread(self) -> None:
        self.app.stop()