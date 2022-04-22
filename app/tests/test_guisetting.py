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

import guisetting as gui
import projectguisetting as pjgui

from const import PROGRAM_NAME, FAVICON_IMAGE_PATH

# -------------------------------------------------------------------------
# Local functions
# -------------------------------------------------------------------------
def test_guisetting() -> None:
    grid_title: str = PROGRAM_NAME
    icon_path: str = FAVICON_IMAGE_PATH
    t = gui.GuiSetting(grid_title, icon_path)

    # 実行開始(表示状態or非表示状態)
    is_hidden_start: bool = False
    t.main(is_hidden_start)

def test_projectguisetting() -> None:
    grid_title: str = PROGRAM_NAME
    icon_path: str = FAVICON_IMAGE_PATH
    t = pjgui.ProjectGuiSetting(grid_title, icon_path)

    # 実行開始(表示状態or非表示状態)
    is_hidden_start: bool = False
    t.main(is_hidden_start)

if __name__ == "__main__":
    # test_guisetting()
    test_projectguisetting()