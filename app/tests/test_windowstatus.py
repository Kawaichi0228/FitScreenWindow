# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from abc import ABC, abstractmethod
import sys

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from util import LIB_DIR
sys.path.append(LIB_DIR)
from windowstate import *
from windowaction import *

# -------------------------------------------------------------------------
# Local functions
# -------------------------------------------------------------------------
def testMoveResizeWindow() -> None:
    # アクティブなウィンドウのハンドルを取得
    hwnd_actvwin = getActiveWinHwnd()

    # 画面のスクリーンサイズを取得
    width = getScreenWidth()
    height = getScreenHeight()
    x = 0
    y = 500

    # ウィンドウのリサイズと移動
    moveResizeWindow(hwnd_actvwin, x, y, width, height)

def testActiveWindow() -> None:
    # 指定したタイトルのhwndを取得
    hwnd_memoapp = getWinHwnd("タイトルなし - メモ帳")

    # 指定ウィンドウをアクティブにする
    activeWindow(hwnd_memoapp)

def testGetWinPostion() -> None:
    # 指定したタイトルのhwndを取得
    hwnd_memoapp = getWinHwnd("タイトルなし - メモ帳")

    # 指定ウィンドウの画面位置を取得
    pos_x = getWinPositionX(hwnd_memoapp)
    pos_y = getWinPositionY(hwnd_memoapp)
    print(pos_x)
    print(pos_y)

def main() -> None:
    testMoveResizeWindow()
    testActiveWindow()
    testGetWinPostion()

if __name__ == "__main__":
    main()