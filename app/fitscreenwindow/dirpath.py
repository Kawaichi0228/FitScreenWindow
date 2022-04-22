# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import os, sys

# -------------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------------
# この実行ファイルのディレクトリパス
if getattr(sys, 'frozen', False): # Pyinstallerでビルドされたか判定
    _this_dir = os.path.dirname(os.path.abspath(sys.executable)) # sys.executableがビルドしたexeのパスを返す
else:
    _this_dir = os.path.dirname(os.path.abspath(__file__))
THIS_DIR = _this_dir

# このディレクトリから指定したディレクトリやファイルパス
LIB_DIR = THIS_DIR + "/lib"