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

# 各ディレクトリ
EXECUTION_DIR = os.getcwd() # 実行ファイルのパスを取得

ROMING_DIR_BEFORE = r"C:\Users"
USER_NAME = os.getlogin()
ROMING_DIR_AFTER = r"AppData\Roaming"
ROMING_DIR = f"{ROMING_DIR_BEFORE}\\{USER_NAME}\\{ROMING_DIR_AFTER}"

root_directory_execution = f"{EXECUTION_DIR}\\app"
if os.path.exists(root_directory_execution):
    ROOT_DIR = root_directory_execution
else:
    root_directory_roming = f"{ROMING_DIR}\\{PROGRAM_NAME}\\app"
    ROOT_DIR = root_directory_roming

SOURCE_DIR = f"{ROOT_DIR}\\src"
IMAGES_DIR = f"{ROOT_DIR}\\images"

# faviconのパス
FAVICON_IMAGE_PATH = f"{IMAGES_DIR}\\favicon.ico"

# config.json(設定ファイル)のパス
CONFIG_JSON_PATH = f"{SOURCE_DIR}\\config.json"