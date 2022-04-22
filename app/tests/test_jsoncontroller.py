#! /usr/bin/env python3.9
# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import sys
from tkinter import messagebox
import subprocess

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from util import (
    LIB_DIR,
    CONFIG_JSON_PATH_TESTCASE1,
    CONFIG_JSON_PATH_TESTCASE2
)

sys.path.append(LIB_DIR)
from jsoncontroller import jsoncontroller

# -------------------------------------------------------------------------
# Local functions
# -------------------------------------------------------------------------
def test_getjsondict() -> None:
    """JSONファイルを読込(dictとして取得)
    テストケース1: 修飾キーなし"""
    jc = jsoncontroller(CONFIG_JSON_PATH_TESTCASE1)
    jsonDict = jc.get_jsondict()

    # jsonDictionaryからホットキーの値を取り出し、実引数へ渡す
    hotkey_windowleft = jsonDict["hotkey"]["windowleft"]
    hotkey_windowright = jsonDict["hotkey"]["windowright"]

    print("json定義キー[ウィンドウ左寄せ]", hotkey_windowleft)
    print("json定義キー[ウィンドウ右寄せ]", hotkey_windowright)


def test_getjsondict2() -> None:
    """JSONファイルを読込(dictとして取得)
    テストケース2: 修飾キーあり"""
    jc = jsoncontroller(CONFIG_JSON_PATH_TESTCASE2)
    jsonDict = jc.get_jsondict()

    windowleft_keydict = jsonDict["hotkey_windowleft"]
    windowright_keydict = jsonDict["hotkey_windowright"]
    print(windowleft_keydict, windowright_keydict)


def test_overwritesavejson() -> None:
    """JSONファイルを上書き保存読込"""
    jc: object = jsoncontroller(CONFIG_JSON_PATH_TESTCASE1)
    json_dict: dict = jc.get_jsondict()

    # 実行時のjsonを格納
    begin_hotkey_windowleft = json_dict["hotkey"]["windowleft"]
    begin_hotkey_windowright = json_dict["hotkey"]["windowright"]

    # 上書きする値をdictに定義
    WRITE_VALUE = "***SAVEOK*** overwrite_after"
    json_dict["hotkey"]["windowleft"] = WRITE_VALUE + "windowleft"
    json_dict["hotkey"]["windowright"] = WRITE_VALUE + "windowright"

    # jsonを上書き
    jc.overwrite_save_json(json_dict)

    # jsonが上書きされたか確認するためにメモ帳でconfig.jsonを開く
    subprocess.run([r"NOTEPAD", CONFIG_JSON_PATH_TESTCASE1])  # 同期実行

    # 上書きの確認メッセージ
    TITLE = "確認"
    MSG = """
        jsonファイルを定義した値で上書きしました。
        config.jsonを開いて、上書きされたことを確認してください。
        (OKボタンを押すと実行時の値へ元に戻します)
        """
    messagebox.showinfo(TITLE, MSG)

    # 実行時のjsonの値へ元に戻す
    json_dict["hotkey"]["windowleft"] = begin_hotkey_windowleft
    json_dict["hotkey"]["windowright"] = begin_hotkey_windowright
    jc.overwrite_save_json(json_dict)


if __name__ == "__main__":
    test_getjsondict()
    test_overwritesavejson()
    test_getjsondict2()
