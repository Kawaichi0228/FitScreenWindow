# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import wx

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class Dialog():
    def __init__(self) -> None:
        self.__root = wx.App()
    
    def showOKOnlyExclamation(self, title, value) -> None:
        wx.MessageBox(value, title, wx.OK|wx.ICON_EXCLAMATION)

    def showOKCancelnfomation(self, value, title, is_cancel_default=False) -> None:
        if is_cancel_default:
            wx.MessageBox(value, title, wx.CANCEL|wx.ICON_INFORMATION|wx.CANCEL_DEFAULT)
        else:
            wx.MessageBox(value, title, wx.CANCEL|wx.ICON_INFORMATION)


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