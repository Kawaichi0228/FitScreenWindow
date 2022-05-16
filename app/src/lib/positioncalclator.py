# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from src.lib.windowstate import (
    getScreenWidth,
    getTaskBarWidth,
    getTaskBarHeight,
    getTaskBarPosition,
    TaskBarPosition,
)
from src.lib.const import MoveResizeDirection
from src.lib.config import Config

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class PositionCalclator:
    # -------------------------------------------------------------------------
    def calclatePositionX(self, direction, width) -> int:
        if direction == MoveResizeDirection.LEFT:
            x = self.__calclatePositionXtoLeft()

            # タスクバーの位置が左設定ならxを足す
            if getTaskBarPosition() == TaskBarPosition.LEFT:
                width_taskbar = getTaskBarWidth()
                return x + width_taskbar
            
            return x

        if direction == MoveResizeDirection.RIGHT:
            x = self.__calclatePositionXtoRight(width)

            # タスクバーの位置が右設定ならxを引く
            if getTaskBarPosition() == TaskBarPosition.RIGHT:
                width_taskbar = getTaskBarWidth()
                return x - width_taskbar

            return x

    def __calclatePositionXtoLeft(self) -> int:
        """ウィンドウ左寄せ"""
        x_left = 0
        x = int(x_left - Config.Position.adjust_x_px)
        return x
    
    def __calclatePositionXtoRight(self, width) -> int:
        """ウィンドウ右寄せ"""
        width_screen = getScreenWidth()
        x_right = width_screen - width
        x = int(x_right + Config.Position.adjust_x_px)
        return x

    # -------------------------------------------------------------------------
    def calclatePositionY(self) -> int:
        y = 0

        # タスクバーの位置が上設定ならyを足す
        if getTaskBarPosition() == TaskBarPosition.TOP:
            height_taskbar = getTaskBarHeight()
            return y + height_taskbar
        
        return y