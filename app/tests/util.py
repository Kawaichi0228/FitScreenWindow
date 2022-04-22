# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import os

# -------------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------------
# この実行ファイルのディレクトリパス
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# このディレクトリから指定したディレクトリやファイルパス
LIB_DIR = THIS_DIR + "/../fitscreenwindow/lib"

CONFIG_JSON_DIR = THIS_DIR
CONFIG_JSON_PATH_TESTCASE1 = CONFIG_JSON_DIR + "/" + "test_config.json"
CONFIG_JSON_PATH_TESTCASE2 = CONFIG_JSON_DIR + "/" + "test_config2.json"