# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import os
from enum import Enum, unique, auto

# -------------------------------------------------------------------------
# Enum
# -------------------------------------------------------------------------
@unique
class MoveResizeDirection(Enum): # base number:1
    """ウィンドウ移動・リサイズ実行時の方向識別子"""
    LEFT = auto()
    RIGHT = auto()

# -------------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------------
# プロジェクトの名前
PROGRAM_NAME = "FitScreenWindow"

# 現在のディレクトリ
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# faviconのパス
IMAGES_DIR = THIS_DIR + r"\..\..\images"
FAVICON_IMAGE_PATH = IMAGES_DIR + r"\favicon.ico"

# config.json(設定ファイル)のパス
CONFIG_JSON_DIR = THIS_DIR + r"\.."
CONFIG_JSON_PATH = CONFIG_JSON_DIR + "/" + "config.json"

# config.jsonの各キー(アイテムをPython側から取り出す用のキー)
JSONKEY_WINDOW_LEFT = "hotkey_windowleft"
JSONKEY_WINDOW_RIGHT = "hotkey_windowright"
JSONKEY_CTRL = "mod_ctrl"
JSONKEY_SHIFT = "mod_shift"
JSONKEY_ALT = "mod_alt"
JSONKEY_HOTKEY = "hotkey"
