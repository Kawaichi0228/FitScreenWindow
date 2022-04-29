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
# TODO: 実行ファイルではなく.venvがある(もしくはワークスペース？)の
# ディレクトリ取得になってしまっている。そのため、"\app" を付加している。
ROOT_DIR = os.getcwd() + r"\app" # 実行ファイルのパスを取得
SOURCE_DIR = ROOT_DIR + r"\src"
IMAGES_DIR = ROOT_DIR + r"\images"

# faviconのパス
FAVICON_IMAGE_PATH = IMAGES_DIR + r"\favicon.ico"

# config.json(設定ファイル)のパス
CONFIG_JSON_PATH = SOURCE_DIR + r"\config.json"
