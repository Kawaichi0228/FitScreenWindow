# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from logging import getLogger
from src.lib.logger import *
logger = getLogger("Log")

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
        self.height_screen = int(height_screen)

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

    # -------------------------------------------------------------------------
    def calclateWidth(self, direction) -> int:
        # メモリした移動・リサイズ方向と今回実行した方向が違う場合は、
        # 画面widthから、メモリしたウィンドウwidthを差し引いたwidthを返す(画面の余白残りにサイズをフィットさせる)
        actvwin = self.getActiveWindowState()
        memorywin = self.__getMemoryWindowState()
        if all([ # all関数: and条件式
            not actvwin["hwnd"] == memorywin["hwnd"],
            not self.__isEqualMemoryDirection(direction),
        ]):
            width = self.__calclateWidthForNotMemory()
            return width

        else:
            width = self.__calclateWidthForCounter(direction)
            return width

    def __calclateWidthForNotMemory(self) -> int:
        """画面widthからメモリしたウィンドウwidthを差し引いたwidthを返す(画面の余白残りにサイズをフィットさせる)"""
        screen_width = getScreenWidth()
        memorywin = self.__getMemoryWindowState()
        memory_width = memorywin["width"]
        adjust_width = Config.Size.adjust_width_px
        width = screen_width - memory_width + adjust_width
        return width

    def __calclateWidthForCounter(self, direction) -> int:
        # 基準Width
        if direction == MoveResizeDirection.LEFT:
            width_base = Config.Size.base_width_toleft_px
        elif direction == MoveResizeDirection.RIGHT:
            width_base = Config.Size.base_width_toright_px

        # 調整用Width
        adjust_width = Config.Size.adjust_width_px

        # カウンタが1回目(初回リサイズ実行時)のときはWidthを加算させない
        cnt = self.cnt.get()
        if cnt == 1:
            width = int(round(width_base + adjust_width))
            return width
        
        # カウンタが2回目以降
        else:
            # リサイズ時に加算するWidthを計算
            # - px/回の設定したwidth値を、cntの回数分だけ倍にするための倍率を定義
            ratio = cnt - 1 # 2回目実行時に加算サイズ×1倍とするため、実行回数cntから-1する

            # - 加算するサイズを計算
            original_add_width = Config.Size.resize_add_width_px * ratio 

            # 逆方向に拡大オプションがtrueなら加算するWidthの符号を逆にする
            if any([
                all([
                    direction == MoveResizeDirection.LEFT,
                    Config.Size.is_reverse_direction_windowleft,
                ]),
                all([
                    direction == MoveResizeDirection.RIGHT,
                    Config.Size.is_reverse_direction_windowright,
                ]),
            ]):
                subtraction_width = original_add_width * (-1)
                add_width = subtraction_width
                
            else:
                add_width = original_add_width

            width = int(round(width_base + add_width + adjust_width))
            return width
    
    # -------------------------------------------------------------------------
    def calclateHeight(self) -> int:
        # タスクバーのHeight分をマイナスするかどうか
        taskbar_position = getTaskBarPosition()
        if any([
            not Config.Size.is_subtract_taskbar, # 「タスクバーのサイズを差し引く」オプションを無効にしている時
            taskbar_position == TaskBarPosition.LEFT, # タスクバー位置が左の時
            taskbar_position == TaskBarPosition.RIGHT, # タスクバー位置が右の時
        ]):
            height = self.__calclateHeightForScreenMax()
            return height

        else:
            height = self.__calclateHeightForTaskbar()
            return height
    
    def __calclateHeightForScreenMax(self) -> int:
        """画面最大のHeightを返す"""
        height = int(self.height_screen) # 画面最大のHeightを返す
        return height

    def __calclateHeightForTaskbar(self) -> int:
        """タスクバーのHeightを差し引いた画面最大のHeightを返す"""
        height_taskbar = getTaskBarHeight()
        height = int(self.height_screen - height_taskbar)
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