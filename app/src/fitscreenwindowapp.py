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
from src.lib.configconverter import ConfigConverter
from src.lib.windowstate import getActiveWinHwnd, isExplorerWindow
from src.lib.errordialog import ErrorDialog
from src.lib.errorhandling import ErrorHandling
from src.lib.config import Size, Position, HotkeyWindowLeft, HotkeyWindowRight
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
        key_converter = ConfigConverter()
        keycombination_windowleft = key_converter.convertHotkeyConfigToKeycode(HotkeyWindowLeft)
        keycombination_windowright = key_converter.convertHotkeyConfigToKeycode(HotkeyWindowRight)

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
    
    def overWriteConfig(self, json_obj) -> None:
        # jsonのvalueからkeycodeへ変換したdictを取得
        json_dict = self.jc.getDictionary(json_obj) # JSONファイルの内容を2次元dictとして取得
        
        # config.pyをjsonで読みとった値で書き換え
        json_size = json_dict["size"]
        Size.resize_max_cnt = json_size["resize_max_cnt"]
        Size.resize_ratio = json_size["resize_ratio"]
        Size.base_width_toleft_px = json_size["base_width_toleft_px"]
        Size.base_width_toright_px = json_size["base_width_toright_px"]
        Size.adjust_width_px = json_size["adjust_width_px"]
        Size.is_subtract_taskbar = json_size["is_subtract_taskbar"]
        
        json_position = json_dict["position"]
        Position.adjust_x_px = json_position["adjust_x_px"]

        json_hotkey_windowleft = json_dict["hotkey_windowleft"]
        HotkeyWindowLeft.mod_ctrl = json_hotkey_windowleft["mod_ctrl"]
        HotkeyWindowLeft.mod_shift = json_hotkey_windowleft["mod_shift"]
        HotkeyWindowLeft.mod_alt = json_hotkey_windowleft["mod_alt"]
        HotkeyWindowLeft.mod_win = json_hotkey_windowleft["mod_win"]
        HotkeyWindowLeft.hotkey = json_hotkey_windowleft["hotkey"]

        json_hotkey_windowright = json_dict["hotkey_windowright"]
        HotkeyWindowRight.mod_ctrl = json_hotkey_windowright["mod_ctrl"]
        HotkeyWindowRight.mod_shift = json_hotkey_windowright["mod_shift"]
        HotkeyWindowRight.mod_alt = json_hotkey_windowright["mod_alt"]
        HotkeyWindowRight.mod_win = json_hotkey_windowright["mod_win"]
        HotkeyWindowRight.hotkey = json_hotkey_windowright["hotkey"]

        assert print("メッセージ: config.jsonからconfig.pyへ変数値の書き換えが完了しました") == None


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
        # config.jsonを読み取り、config.pyの各データクラスを上書きする
        json_service = JsonService()
        json_obj = json_service.read()
        json_service.overWriteConfig(json_obj)

        # スレッド開始
        self.startThread()


# -------------------------------------------------------------------------
# Local functions
# -------------------------------------------------------------------------
def main() -> None:
    app = ApplicationService()
    app.run()

