#! /usr/bin/env python3.9
# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import sys

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from util import LIB_DIR
sys.path.append(LIB_DIR)
from globalhotkey import GlobalHotkey
from keycode import KeyCode

# -------------------------------------------------------------------------
# Local functions
# -------------------------------------------------------------------------
def printA() -> None:
    print("A")

if __name__ == "__main__":
    modifier_keys_list: list = []
    hotkeys_list: list = []

    hk = KeyCode()
    modifier_keys_list.append(hk.MODKEY["CTRL"] + hk.MODKEY["ALT"])
    hotkeys_list.append(hk.getAskkey("B"))
    funcobj = printA

    g = GlobalHotkey(modifier_keys_list, hotkeys_list, funcobj)
    g.startThread()