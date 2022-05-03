# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import wx

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
"""修飾キー・ホットキーとして設定可能とするキーを定義するクラスモジュール"""
class ModifireKey:
    def __init__(self) -> None:
        self.mod_list = []
        self.CTRLKEY = wx.MOD_CONTROL
        self.SHIFTKEY = wx.MOD_SHIFT
        self.ALTKEY = wx.MOD_ALT
        self.WINKEY = wx.MOD_WIN

    def add(self, modkey) -> None:
        self.mod_list.append(modkey)

    def getCombinationKeycode(self) -> int:
        """修飾キーの組み合わせをintとして返す"""
        join_mod = 0
        for mod in self.mod_list:
            join_mod += mod

        mod_combination = join_mod
        return mod_combination


class Hotkey:
    ERR_MSG_TYPEERROR_STR = "String型を引数に指定して下さい"
    
    def __init__(self) -> None:
        self.number = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.alphabet = (
            "a", "b", "c", "d", "e","f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
            "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        )
        self.allow = ("left", "right", "up", "down")

    def getKeyList(self) -> list:
        key_list = []
        key_list.append(self.number)
        key_list.append(self.alphabet)
        key_list.append(self.allow)
        return key_list

    def getKeycode(self, value: str) -> int:
        if any([
            self.__isNumberString(value),
            self.__isAlphabet(value)
        ]): return self.__convertToAskkey(value)

        if self.__isAllow(value): return self.__convertToWxPythonKey(value)

        raise ValueError("引数として与えられたキーが、定義したホットキーリストに含まれていません")

    def __isNumberString(self, value: str) -> bool:
        if not type(value) == str: raise TypeError(self.ERR_MSG_TYPEERROR_STR)
        return True if value in self.number else False

    def __isAlphabet(self, value: str) -> bool:
        if not type(value) == str: raise TypeError(self.ERR_MSG_TYPEERROR_STR)
        value_lower = str.lower(value) # 大文字小文字を区別させない
        return True if value_lower in self.alphabet else False

    def __isAllow(self, value: str) -> bool:
        if not type(value) == str: raise TypeError(self.ERR_MSG_TYPEERROR_STR)
        value_lower = str.lower(value) # 大文字小文字を区別させない
        return True if value_lower in self.allow else False
    
    def __convertToAskkey(self, value: str) -> int:
        """文字列リテラルをasciiコードに変換"""
        value_upper = str.upper(value)
        return ord(value_upper)
        
    def __convertToWxPythonKey(self, value: str) -> int:
        value_lower = str.lower(value) # 大文字小文字を区別させない
        key_dict = {
            "left": wx.WXK_LEFT,
            "right": wx.WXK_RIGHT,
            "down": wx.WXK_DOWN,
            "up": wx.WXK_UP,
        }
        return key_dict[value_lower]
