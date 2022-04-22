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
import Tasktry as task

from const import PROGRAM_NAME, FAVICON_IMAGE_PATH

# -------------------------------------------------------------------------
# Local functions
# -------------------------------------------------------------------------
def test_Tasktry() -> None:
    # インスタンス化
    grid_title: str = PROGRAM_NAME
    icon_path: str = FAVICON_IMAGE_PATH
    t = task.Tasktry(grid_title, icon_path)

    # タスクメニューに表示させる各ボタンの値と処理動作を定義
    root_tkinter = t.gui.get_tkinter()  # tkinterのrootを取得

    Tasktry_VALUE_HOTKEYSETTING = "キー設定"
    Tasktry_dict_hotkeysetting = {
        Tasktry_VALUE_HOTKEYSETTING:
        lambda: root_tkinter.after(0, t.gui.show_gui)
    }
    t.add_items(Tasktry_dict_hotkeysetting)

    Tasktry_VALUE_QUITAPP = "終了"
    Tasktry_dict_quitapp = {
        Tasktry_VALUE_QUITAPP:
        lambda: root_tkinter.after(1, t.stopThread)
    }
    t.add_items(Tasktry_dict_quitapp)

    # メイン処理の実行
    is_hidden_start: bool = True # 非表示状態でtkinterを開始
    t.main(is_hidden_start)


if __name__ == "__main__":
    test_Tasktry()
