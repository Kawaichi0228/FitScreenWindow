# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from src.lib.windowstate import getScreenWidth
from src.lib.const import MoveResizeDirection
from src.lib.config import Config

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class PositionCalclator:
    def calclatePositionX(self, direction, width) -> int:
        if direction == MoveResizeDirection.LEFT:
            return self.calclatePositionXtoLeft()
        if direction == MoveResizeDirection.RIGHT:
            return self.calclatePositionXtoRight(width)

    def calclatePositionXtoLeft(self) -> int:
        """ウィンドウ左寄せ"""
        x_left = 0
        x = int(x_left - Config.Position.adjust_x_px)
        return x
    
    def calclatePositionXtoRight(self, width) -> int:
        """ウィンドウ右寄せ"""
        width_screen = getScreenWidth()
        x_right = width_screen - width
        x = int(x_right + Config.Position.adjust_x_px)
        return x
