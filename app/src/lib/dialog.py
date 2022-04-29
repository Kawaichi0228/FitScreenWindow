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
