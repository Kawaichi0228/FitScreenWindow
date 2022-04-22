#! /usr/bin/env python3.9
# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import sys
from time import sleep

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from util import LIB_DIR
sys.path.append(LIB_DIR)
from moveresizewindow import *
from windowstate import *

# AppService
def test_right() -> None:
    m = MoveResizeWindow()

    sleep(1)

    hwnd = getActiveWinHwnd()
    # MEMO: 1210(activewin_width)が一致していないと右端寄せできない
    x_right = 1920 - 1210
    x = x_right
    y = 0
    width = 1210
    height = 1054
    m.execute(hwnd, x, y, width, height)

if __name__ == "__main__":
    test_right()