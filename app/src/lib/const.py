# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import os
import sys
import getpass
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

# 実行ファイルのディレクトリパスを定義
if __debug__: # デバッグ実行時
    EXECUTION_ROOT_DIR = os.getcwd()
else: # コンパイル実行時
    EXECUTION_ROOT_DIR = os.path.dirname(sys.executable)

# 各ソースファイルのパスを定義
if os.path.exists(f"{EXECUTION_ROOT_DIR}\\app"):
    # ポータブル実行用パス
    FAVICON_IMAGE_PATH = f"{EXECUTION_ROOT_DIR}\\app\\images\\favicon.ico"
    CONFIG_JSON_DIR = f"{EXECUTION_ROOT_DIR}\\app\\src"
    CONFIG_JSON_PATH = f"{CONFIG_JSON_DIR}\\config.json"

else:
    # インストール実行用パス
    USER_NAME = getpass.getuser()
    FAVICON_IMAGE_PATH = f"{EXECUTION_ROOT_DIR}\\favicon.ico"
    CONFIG_JSON_DIR = f"C:\\Users\\{USER_NAME}\\AppData\\Roaming\\{PROGRAM_NAME}"
    CONFIG_JSON_PATH = f"{CONFIG_JSON_DIR}\\config.json"