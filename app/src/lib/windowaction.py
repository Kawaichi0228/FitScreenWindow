# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import win32gui # MEMO: install command[pip install pywin32]

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from src.lib.windowstate import *

# -------------------------------------------------------------------------
# Local functions
# -------------------------------------------------------------------------
def activeWindow(hwnd) -> None:
    """指定ウィンドウをアクティブにさせる"""
    win32gui.SetForegroundWindow(hwnd)

def setNormalState(hwnd):
    """最大化ウィンドウを通常状態に戻す"""
    win32gui.ShowWindow(hwnd,1) # 1:SW_SHOWNORMAL

def setMaximumState(hwnd):
    """ウィンドウを最大化"""
    win32gui.ShowWindow(hwnd,3) # 3:SW_SHOWMAXIMIZED

def setMinimumState(hwnd):
    """ウィンドウを最小化"""
    win32gui.ShowWindow(hwnd,2) # 2:SW_SHOWMINIMIZED

def moveResizeWindow(hwnd, x=None, y=None, width=None, height=None) -> None:
    """指定ウィンドウのサイズ変更及び移動を行う
    Remarks: 最大化されているウィンドウには処理が反映されない

    Parameters:
    ----------
    (各引数省略時): 指定ハンドルウィンドウの現在ステータスを使う
    """
    # ウィンドウが最大化状態だったら標準状態に戻す
    # TODO: ウィンドウstateを取得し、最大化状態のときのみ実行するようにする
    # (If ウィンドウが最大化されていた場合は元サイズに戻す動作を入れる)
    setNormalState(hwnd)

    if x == None: x = getWinPositionX(hwnd)
    if y == None: y = getWinPositionY(hwnd)
    if width == None: width = getWinWidth(hwnd)
    if height == None: height = getWinHeight(hwnd)
    win32gui.MoveWindow(hwnd, x, y, width, height, True)