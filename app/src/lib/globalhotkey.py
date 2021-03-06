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
        self.id_hotkey_list = []

        self.thread = None

    def startThread(self) -> None:
        # threading.Thread Parameter:
        #   daemon=True: スレッドをデーモン化(常駐化)させる ※デーモン=Unix系の常駐プログラムの呼称(Windows系はサービス)
        # (thread.setDaemon(True)でも同じ)
        thread = threading.Thread(
            name="FitScreenWindow", target=self.__root.MainLoop, daemon=True
        )
        thread.start()
        self.thread = thread

    def stopThread(self) -> None:
        for id in self.id_hotkey_list:
            self.UnregisterHotKey(id)
        self.thread = None
        # self.__root.ExitMainLoop() # スレッド終了できるがエラー出てしまう(threading.Event()と.setDaemon(True)を使えば解決できる？)

    def registerHotkey(self, modifier_keys: any, hotkey: any) -> int:
        """ホットキーを登録
        return:
            int: ホットキーID
        """
        id_hotkey = wx.NewIdRef(count=1)
        self.id_hotkey_list.append(id_hotkey)
        self.RegisterHotKey(id_hotkey, modifier_keys, hotkey)
        return id_hotkey

    def bindHotkey(self, bindevent, id_hotkey) -> None:
        # HotkeyのEventHandlerをbind
        self.Bind(wx.EVT_HOTKEY, bindevent, id=id_hotkey)

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
