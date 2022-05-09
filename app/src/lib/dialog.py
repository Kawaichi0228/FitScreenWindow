# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import wx

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class Dialog():
    # MEMO: ★★★超重要メモ★★★
    #   root生成(ex. tkinterのtk.Tk()やwxPythonのwx.App() )は、
    #   全モジュールで1つしか生成できない(？)。エラー出る。
    #   ※wxPythonは、そもそもインスタンス化しなくてもMessageBoxを表示できる
    
    def showOKOnlyExclamation(self, title, value) -> None:
        wx.MessageBox(value, title, wx.OK|wx.ICON_EXCLAMATION)

    def showOKCancelExclamation(self, value, title, is_cancel_default=False) -> bool:
        if is_cancel_default:
            user_input = wx.MessageBox(value, title, wx.CANCEL|wx.ICON_EXCLAMATION|wx.CANCEL_DEFAULT)
        else:
            user_input = wx.MessageBox(value, title, wx.CANCEL|wx.ICON_EXCLAMATION|wx.OK_DEFAULT)

        if user_input == wx.OK: return True
        if user_input == wx.CANCEL: return False

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