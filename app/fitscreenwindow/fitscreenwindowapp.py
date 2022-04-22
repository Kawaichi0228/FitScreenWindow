#! /usr/bin/env python3.9
# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import sys
from abc import ABC, abstractmethod

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from .dirpath import LIB_DIR
sys.path.append(LIB_DIR)

from globalhotkey import GlobalHotkey
from moveresizewindow import *
from sizecalclator import *
from tasktray import Tasktray
from const import (
    MoveResizeDirection,
    CONFIG_JSON_PATH,
    PROGRAM_NAME,
    FAVICON_IMAGE_PATH,
    JSONKEY_WINDOW_LEFT,
    JSONKEY_WINDOW_RIGHT
)
from jsoncontroller import JsonController
from jsontokeycode import JsonToKeycode
from windowstate import getActiveWinHwnd, isExplorerWindow


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
        # TODO: isSubsrtact...をjsonconfig化する
        height = self.size.calclateHeight(isSubtractTaskBar=True) # heightはタスクバーのheight分をマイナスする

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
        # グローバルホットキー
        g = GlobalHotkey()
        self.g = g

    def startThread(self) -> None:
        """グローバルホットキー実行用のスレッド"""
        mr = MoveResizeWindowService()

        # HACK: jsonのItemを読み込み、オブジェクトデータを保持しておくサービスクラスを作ったほうがよい
        # jsonを読み込む
        jc = JsonController(CONFIG_JSON_PATH)
        json_dict = jc.getDictionary() # JSONファイルの内容を2次元dictとして取得
        # jsonのvalueからkeycodeへ変換したdictを取得
        json_to_keycode = JsonToKeycode()
        keycombination_windowleft = json_to_keycode.convert(json_dict[JSONKEY_WINDOW_LEFT])
        keycombination_windowright = json_to_keycode.convert(json_dict[JSONKEY_WINDOW_RIGHT])

        # 登録するホットキーとそれにバインドするイベント処理を定義
        register = {}

        # ------ windowleft ------ 
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

    def stopThread(self) -> None:
        self.g.stopThread()


class TasktrayService(IThread):
    def __init__(self) -> None:
        # タスクメニュー
        favicon_path_ = FAVICON_IMAGE_PATH
        title_ = PROGRAM_NAME
        t = Tasktray(favicon_path_, title_)
        self.t = t

    def startThread(self) -> None:
        """タスクメニュー実行用のスレッド"""
        self.t.startThread()

    def stopThread(self) -> None:
        self.t.stopThread()


class ApplicationService(IThread):
    def __init__(self) -> None:
        g_service = GlobalHotkeyService()
        self.g_service = g_service

        t_service = TasktrayService()
        self.t_service = t_service

    def startThread(self) -> None:
        self.g_service.startThread()

        # タスクトレイに表示させるitemを定義
        self.t_service.t.addItem("Exit", self.stopThread)
        self.t_service.startThread() # タスクトレイのスレッド開始

    def stopThread(self) -> None:
        self.g_service.stopThread()
        self.t_service.stopThread()

    def run(self) -> None:
        # HACK: ここにjson読み取りを記述すべきか？
        self.startThread()


def main() -> None:
    app = ApplicationService()
    app.run()

