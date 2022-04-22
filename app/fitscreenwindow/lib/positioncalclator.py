# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from dataclasses import dataclass

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from windowstate import getScreenWidth
from const import MoveResizeDirection

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
@dataclass(frozen=False) # False: セッタ可能にする
class Position:
    """PositionCalclator専用のパラメータオブジェクト"""
    # MEMO: jsonの読込失敗時等のために初期値を設定している
    # TODO: 将来的にJSONからconfigとして変更できるようにする
    adjust_x_px: int = 5 # なぜか完全に画面にぴったりフィットしないため、その調整用(恐らくウィンドウの角丸枠のサイズ？)

class PositionCalclator:
    def calclatePositionX(self, direction, width) -> int:
        if direction == MoveResizeDirection.LEFT:
            return self.calclatePositionXtoLeft()
        if direction == MoveResizeDirection.RIGHT:
            return self.calclatePositionXtoRight(width)

    def calclatePositionXtoLeft(self) -> int:
        """ウィンドウ左寄せ"""
        x_left = 0
        x = int(x_left - Position.adjust_x_px)
        return x
    
    def calclatePositionXtoRight(self, width) -> int:
        """ウィンドウ右寄せ"""
        width_screen = getScreenWidth()
        x_right = width_screen - width
        x = int(x_right + Position.adjust_x_px)
        return x
