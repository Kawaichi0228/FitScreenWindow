# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from src.lib.logger import logger
from src.lib.windowstate import *
from src.lib.counter import *
from src.lib.const import MoveResizeDirection
from src.lib.config import Config

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class SizeCalclatorAtCounter:
    """ホットキーを押下するたびに段階的にリサイズさせるためのカウンタを用意し、
    そのカウンタに基づきサイズを計算する"""
    def __init__(self) -> None:
        cnt = Counter(base=1)
        self.cnt = cnt

        height_screen = getScreenHeight()
        self.height = int(height_screen)

        self.memoryWindowState = {
            "hwnd": "",
            "xy": None,
            "width": 0,
        }

        self.memoryExecuteDirection = 0
    # -------------------------------------------------------------------------
    def resetCounterIfNeeded(self, direction) -> None:
        """リサイズカウンタの初期化をするか定義した条件式から判定し、Trueであればリセットする"""
        if self.__needsResetCounter(direction):
            self.cnt.reset()
            logger.info(f"定義したリセット条件に一致したため、カウンタをリセットしました cnt:{self.cnt.get()}")

    def calclateWidth(self, direction) -> int:
        # メモリした移動・リサイズ方向と今回実行した方向が違う場合は、
        # 画面widthから、メモリしたウィンドウwidthを差し引いたwidthを返す(画面の余白残りにサイズをフィットさせる)
        actvwin = self.getActiveWindowState()
        memorywin = self.__getMemoryWindowState()
        if all([ # all関数: and条件式
            not actvwin["hwnd"] == memorywin["hwnd"],
            not self.__isEqualMemoryDirection(direction),
        ]):
            screen_width = getScreenWidth()
            memorywin = self.__getMemoryWindowState()
            memory_width = memorywin["width"]
            width = screen_width - memory_width + Config.Size.adjust_width_px
            return width

        # リサイズ時に加算するWidthを計算
        add_width = Config.Size.resize_add_width_px * self.cnt.get() # px/回の設定したwidth値を、cntの回数分だけ倍にする

        if direction == MoveResizeDirection.LEFT:
            width_base = Config.Size.base_width_toleft_px
        elif direction == MoveResizeDirection.RIGHT:
            width_base = Config.Size.base_width_toright_px

        width = int(round(width_base + add_width + Config.Size.adjust_width_px))
        return width

    def calclateHeight(self) -> int:
        # configのintをboolへ変換
        isSubtractTaskBar = True if Config.Size.is_subtract_taskbar == 1 else False

        # タスクバーのheight分をマイナスするかどうか
        if isSubtractTaskBar:
            hwnd = getTaskBarHwnd()
            height_taskbar = getWinHeight(hwnd)
            height = int(self.height - height_taskbar)
            return height

        else:
            height = int(self.height)
            return height
    # -------------------------------------------------------------------------
    def __needsResetCounter(self, direction) -> bool:
        """段階リサイズ用カウンタの初期化条件を定義し、満たすならTrueを返す"""
        actvwin = self.getActiveWindowState()
        memorywin = self.__getMemoryWindowState()

        if not self.__isEqualMemoryDirection(direction): return True # メモリした移動・リサイズ方向と今回実行した方向が違う場合
        if self.cnt.get() > Config.Size.resize_max_cnt: return True # 設定したリサイズ上限値を超えていた場合
        if not actvwin["hwnd"] == memorywin["hwnd"]: return True # 前回処理したウィンドウと違うウィンドウだった場合
        if not actvwin["xy"] == memorywin["xy"]: return True # 前回処理後の位置から移動していた場合
        return False

    @staticmethod
    def getActiveWindowState() -> dict:
        activeHwnd = getActiveWinHwnd()
        activeWindowPosition_X = getWinPositionX(activeHwnd)
        activeWindowPosition_Y = getWinPositionY(activeHwnd)
        activeWindowPosition = (activeWindowPosition_X, activeWindowPosition_Y)
        activeWidth = getWinWidth(activeHwnd)
        state = {
            "hwnd": activeHwnd,
            "xy": activeWindowPosition,
            "width": activeWidth,
        }
        return state
    
    def __getMemoryWindowState(self) -> dict:
        return self.memoryWindowState
    
    def setMemoryWindowState(self, state) -> None:
        self.memoryWindowState = state
        
    def setMemoryMoveResizeDirection(self, direction) -> None:
        self.memoryExecuteDirection = direction
        
    def __isEqualMemoryDirection(self, direction) -> bool:
        """移動・リサイズ方向がメモリした方向と同一か判定"""
        if self.memoryExecuteDirection == 0: return True # 初期値状態のときは強制True(まだ1度も移動・リサイズが実行されていない状態)
        if direction == self.memoryExecuteDirection: return True
        return False