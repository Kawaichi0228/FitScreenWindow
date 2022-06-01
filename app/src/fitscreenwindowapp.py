#! /usr/bin/env python3.9
# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from abc import ABC, abstractmethod

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from logging import getLogger
from src.lib.logger import *
logger = getLogger("Log")

from src.lib.globalhotkey import GlobalHotkey
from src.lib.moveresizewindow import MoveResizeWindowAtCounter
from src.lib.sizecalclator import SizeCalclatorAtCounter
from src.lib.positioncalclator import PositionCalclator
from src.lib.test_tasktray import TaskMenuItem, CreateTaskTray
from src.lib.windowstate import getActiveWinHwnd, isExplorerWindow
from src.lib.dialog import ErrorDialog
from src.lib.errorhandling import ErrorHandling
from src.lib.config import Config, ConfigJsonRepository, ConfigGuiService
from src.lib.const import (
    MoveResizeDirection,
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

        pos = PositionCalclator()
        self.pos = pos

        mr = MoveResizeWindowAtCounter(size)
        self.mr = mr

    def toLeft(self) -> None:
        direction = MoveResizeDirection.LEFT
        self.__moveResize(direction)

    def toRight(self) -> None:
        direction = MoveResizeDirection.RIGHT
        self.__moveResize(direction)

    def __moveResize(self, direction_) -> None:
        # アクティブなウィンドウがエクスプローラーなら終了
        hwnd_activewin = getActiveWinHwnd()
        if isExplorerWindow(hwnd_activewin):
            return

        hwnd = hwnd_activewin
        direction = direction_
        y = self.pos.calclatePositionY()
        height = self.size.calclateHeight()

        # リサイズの実行
        logger.info(f"移動・リサイズ処理実行直前のcnt:{self.size.cnt.get()}")
        self.mr.execute(direction, hwnd, y, height)


class IThread(ABC):
    @abstractmethod
    def __init__(self) -> None: ...

    @abstractmethod
    def startThread(self) -> None: ...

    @abstractmethod
    def stopThread(self) -> None: ...


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
                "func": mr.toLeft,
            }
        }
        register.update(register_windowleft)
        # グローバルホットキーを登録
        id_hotkey1 = self.g.registerHotkey(
            register[dictkey_windowleft]["modifierkeys"],
            register[dictkey_windowleft]["hotkey"],
        )
        self.g.registerEvent1(register[dictkey_windowleft]["func"])
        eve = self.g.bindEvent1
        self.g.bindHotkey(eve, id_hotkey1)

        # ------ windowright ------
        # ホットキーとイベント処理内容の定義
        dictkey_windowright = "windowright"
        register_windowright = {
            dictkey_windowright: {
                "modifierkeys": keycombination_windowright["mod_combination"],
                "hotkey": keycombination_windowright["hotkey"],
                "func": mr.toRight,
            }
        }
        register.update(register_windowright)
        # グローバルホットキーを登録
        id_hotkey2 = self.g.registerHotkey(
            register[dictkey_windowright]["modifierkeys"],
            register[dictkey_windowright]["hotkey"],
        )
        self.g.registerEvent2(register[dictkey_windowright]["func"])
        eve = self.g.bindEvent2
        self.g.bindHotkey(eve, id_hotkey2)

        # スレッド開始
        self.g.startThread()
        logger.info("グローバルホットキーのスレッドを開始しました")

    def stopThread(self) -> None:
        self.g.stopThread()
        logger.info("グローバルホットキーのスレッドを停止しました")


class TasktrayService(IThread):
    def __init__(self) -> None:
        tooltip = PROGRAM_NAME
        favicon_path = FAVICON_IMAGE_PATH

        task = TaskMenuItem()
        task.add("test", self.pri)
        item_list = task.get()

        t = CreateTaskTray(tooltip, favicon_path, item_list)
        self.t = t

    @staticmethod
    def pri() -> None:
        print("sgf")

    def startThread(self) -> None:
        """タスクメニュー実行用のスレッド"""
        self.t.start()

        #try:
        #    favicon_obj = self.t.readFavicon()
        #    logger.info("favicon.icoの読込が正常に完了しました")
        #except FileNotFoundError:
        #    ErrorDialog().showFileNotFound("favicon.ico")
        #    ErrorHandling().quitApp()

        #logger.info("タスクトレイのスレッドを開始します")
        #self.t.startThread(favicon_obj)

    def stopThread(self) -> None:
        self.t.stopThread()

    def addItem(self, value, on_click_function) -> None:
        self.t.addItem(value, on_click_function)


class ApplicationService(IThread):
    def __init__(self) -> None:
        g_service = GlobalHotkeyService()
        self.g_service = g_service

        t_service = TasktrayService()
        self.t_service = t_service

        gui_service = ConfigGuiService(self.g_service)
        self.gui_service = gui_service

    def startThread(self) -> None:
        # グローバルホットキーのスレッドを開始
        self.g_service.startThread()

        # タスクトレイに表示させるitemを定義
        #self.t_service.addItem("設定", self.gui_service.start)
        #self.t_service.addItem("終了", self.stopThread)

        # タスクトレイのスレッドを開始
        self.t_service.startThread()

    def stopThread(self) -> None:
        self.g_service.stopThread()
        #self.t_service.stopThread()

    def run(self) -> None:
        # config.jsonから値を読み取り、jsonのValueが格納されたDictを取得
        json_repository = ConfigJsonRepository()

        # config.pyの各データクラスの値を上書きする
        json_repository.setupConfigPython()

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
    mutex = win32event.CreateMutex(sa, False, "unique-string...")
    error = win32api.GetLastError()
    if not error == 0:  # 既に起動している場合
        sys.exit(-1)

    # アプリ起動
    app = ApplicationService()
    app.run()

