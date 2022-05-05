# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import wx
import threading

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class GlobalHotkey(wx.Frame):
    def __init__(self) -> None:
        self.__root = wx.App(False)  # MEMO:移動禁止(wx.Appを作成してからsuperでインスタンス化する必要があるため)
        super(GlobalHotkey, self).__init__(None)

    def startThread(self) -> None:
        thread = threading.Thread(target=self.__root.MainLoop)
        thread.start()

    def stopThread(self) -> None: # TODO: スレッド終了できるがエラー出ている(threading.Event()と.setDaemon(True)を使えば解決できる？)
        self.__root.ExitMainLoop()

    def registerHotkey(self, modifier_keys: any, hotkey: any) -> int:
        """ホットキーを登録
        return:
            int: ホットキーID
        """
        id_hotkey = wx.NewIdRef(count=1)
        self.RegisterHotKey(id_hotkey, modifier_keys, hotkey)
        return id_hotkey

    def bindHotkey(self, bindevent, id_hotkey) -> None:
        # HotkeyのEventHandlerをbind
        self.Bind(
            wx.EVT_HOTKEY, bindevent, id=id_hotkey
        )

    # -------------------------------------------------------------------------
    """ホットキー押下時のイベントを登録
    ※ホットキー押下時のイベントハンドラを受け取るため、self, event の2つの引数が必須
    <ex.> def foo(self, event) -> None:
    """
    def bindEvent1(self, event) -> None:
        return self.func1()
    def bindEvent2(self, event) -> None:
        return self.func2()
    def registerEvent1(self, func) -> None:
        self.func1 = func
    def registerEvent2(self, func) -> None:
        self.func2 = func