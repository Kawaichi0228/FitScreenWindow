# MEMO: 「import logging」は禁止
#   理由: logging.info("xxx") と logger.info("xxx") と書き(読み)間違え防止
import os
from datetime import datetime
from logging import getLogger, basicConfig, StreamHandler, FileHandler, Formatter
from logging import INFO, DEBUG, NOTSET

# ロガーオブジェクト(モジュール関数 getLogger を介してインスタンス化)
# MEMO: getLogger("Log") のようにLogger名(今回は"Log")を指定した上で、
#   複数モジュール間で同じくgetLoggerを宣言すれば、同じPythonインタプリタ
#   プロセス上で動いている限り、複数モジュール間で跨いで使うことができる
logger = getLogger("Log")
logger.setLevel(DEBUG)

# ストリームハンドラの設定(標準出力ストリーム)
stream_handler = StreamHandler() # コンソールへログを出力
stream_handler.setLevel(DEBUG)
formatter = Formatter("%(levelname)s %(message)s")
stream_handler.setFormatter(formatter)

# 保存先の有無チェック
if not os.path.isdir('./Log'):
    os.makedirs('./Log', exist_ok=True)

# ファイルハンドラの設定
file_handler = FileHandler(
    f"./Log/log{datetime.now():%Y%m%d%H%M%S}.log" # ファイルへログを出力
)
file_handler.setLevel(DEBUG)
formatter = Formatter("%(asctime)s@ %(name)s [%(levelname)s] %(funcName)s: %(message)s")
file_handler.setFormatter(formatter)

# ルートロガーの設定
basicConfig(level=NOTSET, handlers=[stream_handler, file_handler])

# log example.
#    logger.info("info")
#    logger.debug("debug")
#    logger.warn("warn")
#    logger.error("error")
#    logger.critical("critical")