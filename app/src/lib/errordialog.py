# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from src.lib.dialog import Dialog

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class ErrorDialog():
    ERROR_COMMON_TITLE = "Fit Screen Window - エラー"
    ERROR_UNKNOWN_PREFIX = "不明なエラー: "
    ERROR_UNKNOWN_DESCRIPTION = "エラーが発生しました"
    ERROR_FILENOTFOUND_PREFIX = "ファイル読込エラー: "
    ERROR_FILENOTFOUND_SUFFIX = " が見つかりません"

    def showUnknown(self) -> None:
        Dialog().showOKOnlyExclamation(
            self.ERROR_COMMON_TITLE,
            f"{self.ERROR_UNKNOWN_PREFIX}{self.ERROR_UNKNOWN_DESCRIPTION}"
        )

    def showFileNotFound(self, filename) -> None:
        Dialog().showOKOnlyExclamation(
            self.ERROR_COMMON_TITLE, self.__formatFileNotFound(filename)
        )

    def __formatFileNotFound(self, filename) -> str:
        return self.ERROR_FILENOTFOUND_PREFIX + \
            filename + self.ERROR_FILENOTFOUND_SUFFIX