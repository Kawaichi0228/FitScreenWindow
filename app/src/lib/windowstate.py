# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from enum import Enum, unique
import win32gui # MEMO: install command[pip install pywin32]
import pyautogui

# -------------------------------------------------------------------------
# Local functions
# -------------------------------------------------------------------------
def getActiveWinHwnd() -> any:
    return win32gui.GetForegroundWindow()

def getWinHwnd(win_title, class_name=None) -> any:
    """指定したウィンドウのハンドルを取得
    Remarks: 最小化されているウィンドウのタイトルは取得できない
    """
    return win32gui.FindWindow(class_name, win_title)

def getWinClass(hwnd) -> str:
    """指定したウィンドウハンドルのクラス名を取得"""
    return win32gui.GetClassName(hwnd)

def getWinPositionX(hwnd, is_right=False) -> int:
    rect = win32gui.GetWindowRect(hwnd)
    if is_right:
        return rect[2]
    else:
        return rect[0]

def getWinPositionY(hwnd, is_bottom=False) -> int:
    rect = win32gui.GetWindowRect(hwnd)
    if is_bottom:
        return rect[3]
    else:
        return rect[1]

def getWinWidth(hwnd) -> int:
    (x1, y1, x2, y2) = win32gui.GetWindowRect(hwnd)
    width = x2 - x1
    return width

def getWinHeight(hwnd) -> int:
    (x1, y1, x2, y2) = win32gui.GetWindowRect(hwnd)
    height = y2 - y1
    return height

def getScreenWidth() -> int:
    screen_w, screen_h = pyautogui.size()
    return screen_w

def getScreenHeight() -> int:
    screen_w, screen_h = pyautogui.size()
    return screen_h

def getScreenPositionX() -> dict:
    left = 0 # 画面左端
    right = getScreenWidth() # 画面右端
    position = {
        "left": left,
        "right": right,
    }
    return position

def isMinimumState(hwnd) -> bool:
    """ウィンドウが最小化状態か判定"""
    return win32gui.IsIconic(hwnd)

def isMaximumState(hwnd) -> bool:
    """ウィンドウが最大化状態か判定"""
    return # TODO: 最大化状態か判定を取得したい

def isExplorerWindow(hwnd) -> bool:
    """hwndがエクスプローラであるか判定"""
    class_name = getWinClass(hwnd)
    return True if class_name == "WorkerW" else False

def getActiveWinWidth() -> int:
    """アクティブなウィンドウのサイズを取得"""
    hwnd_actvwin = getActiveWinHwnd()
    actvwin_width = getWinWidth(hwnd_actvwin)
    return actvwin_width

def getTaskBarHwnd() -> any:
    """タスクバーのhwndを取得"""
    hwnd = win32gui.FindWindowEx(None, None, "Shell_TrayWnd", None)
    return hwnd

def getTaskBarHeight() -> int:
    hwnd = getTaskBarHwnd()
    height_taskbar = getWinHeight(hwnd)
    return height_taskbar

def getTaskBarWidth() -> int:
    hwnd = getTaskBarHwnd()
    width_taskbar = getWinWidth(hwnd)
    return width_taskbar

@unique
class TaskBarPosition(Enum):
    LEFT = 1
    TOP = 2
    RIGHT = 3
    BOTTOM = 4

def getTaskBarPosition() -> any:
    """タスクバー位置(上下左右)をEnum識別子で返す"""
    hwnd = getTaskBarHwnd()
    x_left = getWinPositionX(hwnd)
    y_top = getWinPositionY(hwnd)
    x_right = getWinPositionX(hwnd, is_right=True)
    y_bottom = getWinPositionY(hwnd, is_bottom=True)

    # MEMO: 「タスクバーを自動的に隠す」に設定していると数値マイナスに
    #   なるため、判定を0以下にしている
    if all([x_left <= 0, y_top <= 0]):
        if x_right > y_bottom:
            return TaskBarPosition.TOP
        else:
            return TaskBarPosition.LEFT
         
    if x_left == 0: return TaskBarPosition.BOTTOM
    if y_top == 0: return TaskBarPosition.RIGHT