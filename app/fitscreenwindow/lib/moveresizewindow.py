# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from windowaction import moveResizeWindow
from positioncalclator import PositionCalclator

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class MoveResizeWindowAtCounter:
    """widthのみ、移動・リサイズ処理の実行直前にカウンターの情報を取得したあと計算させている"""
    def __init__(self, SizeCalclatorAtCounter) -> None:
        size = SizeCalclatorAtCounter
        self.size = size

        pos = PositionCalclator()
        self.pos = pos

    def execute(self, direction, hwnd, y, height) -> None:
        # Initialize
        self.size.resetCounterIfNeeded(direction)

        # MainProcess
        # MEMO: widthはカウンター処理(Initializeのリセットや、Finalizeのインクリメント)の関係で、処理直前に計算している
        width = self.size.calclateWidth(direction)
        x = self.pos.calclatePositionX(direction, width)

        # - ウィンドウ移動・リサイズの実行
        moveResizeWindow(hwnd, x, y, width, height)

        # Finalize
        # - アクティブウィンドウのハンドル・位置(xy)をメモリ
        state = self.size.getActiveWindowState()
        self.size.setMemoryWindowState(state)

        # - 実行したウィンドウの移動・リサイズ方向をメモリ
        self.size.setMemoryMoveResizeDirection(direction)

        # - リサイズカウンタのインクリメント
        self.size.cnt.increment()