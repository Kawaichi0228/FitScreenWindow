# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from dataclasses import dataclass

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from windowstate import *
from counter import *
from const import MoveResizeDirection

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
@dataclass(frozen=False) # False: セッタ可能にする
class Size:
    """SizeCalclatorAtCounter専用のパラメータオブジェクト"""
    # MEMO: jsonの読込失敗時等のために初期値を設定している
    # TODO: 将来的にJSONからconfigとして変更できるようにする
    resize_max_cnt: int = 4 # 段階リサイズを実行できる最大回数
    resize_ratio: float = 3 # リサイズごと(カウンタと連動)の拡大倍率(基準サイズから×n倍するか)
    base_width_toleft_px: int = 500 # 初期リサイズ時のウィンドウサイズ
    base_width_toright_px: int = 500 # 初期リサイズ時のウィンドウサイズ
    adjust_width_px: int = 15 # なぜか完全に画面にぴったりフィットしないため、その調整用(恐らくウィンドウの枠のサイズ？)

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
            assert print(f"定義したリセット条件に一致したため、カウンタをリセットしました cnt:{self.cnt.get()}") == None

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
            width = screen_width - memory_width + Size.adjust_width_px
            return width

        # リサイズWidthを計算
        base_magni = 1 # 倍率100%から開始
        magni = (self.cnt.get() / 10) * Size.resize_ratio # 整数intのカウンタを取得し、floatの0.n単位にしている
        width_magnification = base_magni + magni # 1.n倍の形式へフォーマット

        if direction == MoveResizeDirection.LEFT:
            width_base = Size.base_width_toleft_px
        elif direction == MoveResizeDirection.RIGHT:
            width_base = Size.base_width_toright_px

        width = int(round(width_base * width_magnification + Size.adjust_width_px))
        return width

    def calclateHeight(self, isSubtractTaskBar=False) -> int:
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
        if self.cnt.get() > Size.resize_max_cnt: return True # 設定したリサイズ上限値を超えていた場合
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