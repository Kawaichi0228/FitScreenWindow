#! /usr/bin/env python3.9
# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from abc import ABC, abstractmethod

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from src.lib.globalhotkey import GlobalHotkey
from src.lib.moveresizewindow import MoveResizeWindowAtCounter
from src.lib.sizecalclator import SizeCalclatorAtCounter
from src.lib.tasktray import Tasktray
from src.lib.jsoncontroller import JsonController
from src.lib.windowstate import getActiveWinHwnd, isExplorerWindow
from src.lib.errordialog import ErrorDialog
from src.lib.errorhandling import ErrorHandling
from src.lib.config import Config, ConfigJsonToPython
from src.lib.keylist import Hotkey
from src.lib.const import (
    MoveResizeDirection,
    CONFIG_JSON_PATH,
    PROGRAM_NAME,
    FAVICON_IMAGE_PATH,
)


# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class MoveResizeWindowService:
    """ウィンドウ移動・リサイズの実行クラス"""
    def __init__(self) -> None:
        size = SizeCalclatorAtCounter()
        self.size = size
        self.mr = MoveResizeWindowAtCounter(size)
    
    def toLeft(self) -> None:
        direction = MoveResizeDirection.LEFT
        self.__moveResize(direction)

    def toRight(self) -> None:
        direction = MoveResizeDirection.RIGHT
        self.__moveResize(direction)
    
    def __moveResize(self, direction_) -> None:
        # アクティブなウィンドウがエクスプローラーなら終了
        hwnd_activewin = getActiveWinHwnd()
        if isExplorerWindow(hwnd_activewin): return

        hwnd = hwnd_activewin
        direction = direction_
        y = 0
        height = self.size.calclateHeight()

        # リサイズの実行
        assert print(f"移動・リサイズ処理実行直前のcnt:{self.size.cnt.get()}") == None
        self.mr.execute(direction, hwnd, y, height)


class IThread(ABC):
    @abstractmethod
    def __init__(self) -> None: pass

    @abstractmethod
    def startThread(self) -> None: pass

    @abstractmethod
    def stopThread(self) -> None: pass


class GlobalHotkeyService(IThread):
    def __init__(self) -> None:
        g = GlobalHotkey()
        self.g = g

    def startThread(self) -> None:
        """グローバルホットキー実行用のスレッド"""
        mr = MoveResizeWindowService()
        
        # Config.pyに格納された各ホットキーの値をKeycodeへ変換し、dictとして取得
        keycombination_windowleft = Config.getKeycodeforHotkeyWindowLeft()
        keycombination_windowright = Config.getKeycodeforHotkeyWindowRight()

        # 登録するホットキーとそれにバインドするイベント処理を定義
        register = {}

        # ------ windowleft ------
        # ホットキーとイベント処理内容の定義
        dictkey_windowleft = "windowleft"
        register_windowleft = {
            dictkey_windowleft: {
                "modifierkeys": keycombination_windowleft["mod_combination"],
                "hotkey": keycombination_windowleft["hotkey"],
                "func": mr.toLeft
            }
        }
        register.update(register_windowleft)
        # グローバルホットキーを登録
        self.g.registerHotkey(
            register[dictkey_windowleft]["modifierkeys"],
            register[dictkey_windowleft]["hotkey"]
        )
        self.g.registerEvent1(register[dictkey_windowleft]["func"])
        eve = self.g.bindEvent1
        self.g.bindHotkey(eve)

        # ------ windowright ------ 
        # ホットキーとイベント処理内容の定義
        dictkey_windowright = "windowright"
        register_windowright = {
            dictkey_windowright: {
                "modifierkeys": keycombination_windowright["mod_combination"] ,
                "hotkey": keycombination_windowright["hotkey"],
                "func": mr.toRight
            }
        }
        register.update(register_windowright)
        # グローバルホットキーを登録
        self.g.registerHotkey(
            register[dictkey_windowright]["modifierkeys"],
            register[dictkey_windowright]["hotkey"]
        )
        self.g.registerEvent2(register[dictkey_windowright]["func"])
        eve = self.g.bindEvent2
        self.g.bindHotkey(eve)

        # スレッド開始
        self.g.startThread()
        assert print("メッセージ: グローバルホットキーのスレッドを開始しました") == None

    def stopThread(self) -> None:
        self.g.stopThread()


class TasktrayService(IThread):
    def __init__(self) -> None:
        favicon_path_ = FAVICON_IMAGE_PATH
        title_ = PROGRAM_NAME
        t = Tasktray(favicon_path_, title_)
        self.t = t

    def startThread(self) -> None:
        """タスクメニュー実行用のスレッド"""
        try:
            favicon_obj = self.t.readFavicon()
            assert print("メッセージ: favicon.icoの読込が正常に完了しました") == None
        except FileNotFoundError:
            ErrorDialog().showFileNotFound("favicon.ico")
            ErrorHandling().quitApp()

        assert print("メッセージ: タスクトレイのスレッドを開始します") == None
        self.t.startThread(favicon_obj)

    def stopThread(self) -> None:
        self.t.stopThread()
    
    def addItem(self, value, on_click_function) -> None:
        self.t.addItem(value, on_click_function)


class JsonService:
    def __init__(self) -> None:
        jc = JsonController(CONFIG_JSON_PATH)
        self.jc = jc
    
    def read(self) -> object:
        # jsonファイルを読み込む
        try:
            json_obj = self.jc.read()
            assert print("メッセージ: config.jsonの読込が正常に完了しました") == None
        except FileNotFoundError:
            ErrorDialog().showFileNotFound("config.json")
            ErrorHandling().quitApp()
        return json_obj

    def setupConfig(self, json_dict) -> None:
        # config.pyをjsonで読みとった値で書き換え
        config_json = ConfigJsonToPython(json_dict)
        config_json.setupConfig()
        assert print("メッセージ: config.jsonからconfig.pyへ変数値の書き換えが完了しました") == None

    def getDictJson(self, json_obj) -> dict:
        """jsonのvalueをkeycodeへ変換した2次元Dictを取得"""
        return self.jc.getDictionary(json_obj)


class ApplicationService(IThread):
    def __init__(self) -> None:
        g_service = GlobalHotkeyService()
        self.g_service = g_service

        t_service = TasktrayService()
        self.t_service = t_service

    def startThread(self) -> None:
        self.g_service.startThread()

        # タスクトレイに表示させるitemを定義
        self.t_service.addItem("Exit", self.stopThread)
        self.t_service.startThread()

    def stopThread(self) -> None:
        self.g_service.stopThread()
        self.t_service.stopThread()

    def run(self) -> None:
        # config.jsonから値を読み取り
        json_service = JsonService()
        json_object = json_service.read()

        # 生成されたObjectから、jsonのValueが格納されたDictを取得
        json_dict = json_service.getDictJson(json_object)

        # config.pyの各データクラスの値を上書きする
        json_service.setupConfig(json_dict)

        # スレッド開始
        self.startThread()


# -------------------------------------------------------------------------
# Local functions
# -------------------------------------------------------------------------
def main() -> None:
    # 多重起動防止(既に起動しているか判定し、起動していたら起動せずに終了)
    import sys, win32api, win32security, win32event
    sa = win32security.SECURITY_ATTRIBUTES()
    sa.SECURITY_DESCRIPTOR.SetSecurityDescriptorDacl(True, None, False)
    mutex = win32event.CreateMutex(sa, False, 'unique-string...')
    error = win32api.GetLastError()
    if not error == 0: # 既に起動している場合
        sys.exit(-1)

    # アプリ起動
    app = ApplicationService()
    app.run()

