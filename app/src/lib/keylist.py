# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import wx
import itertools

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

    def addCombination(self, modkey) -> None:
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
        # --- 文字列キー ---
        # MEMO: "\\": バックスラッシュ単体はraw文字列不可のため、エスケープ文字(\)でエスケープしている
        self.alphabet = (
            "A", "B", "C", "D", "E","F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        )
        self.number = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        self.symbol = ("_", "-", "^", "\\", "@", "[", ";", ":", "]", ",", ".", "/")
        # --- 制御キー ---
        self.control = ("Left", "Right", "Up", "Down", "Space", "Tab")

    def getKeyList(self) -> list:
        # MEMO: append位置 = 返されるリストのソート順が決まる
        key_list = []
        key_list.append(self.alphabet)
        key_list.append(self.symbol)
        key_list.append(self.number)
        key_list.append(self.control)
        key_list = list(itertools.chain.from_iterable(key_list)) # 多次元リストを一次元化
        return key_list

    def getKeycode(self, value: str) -> int:
        if any([
            self.__isNumberString(value),
            self.__isAlphabet(value),
        ]): return self.__convertToAskkey(value)

        if self.__isSymbol(value): return self.__convertToAskkey_individual(value)

        if self.__isControl(value): return self.__convertToWxPythonKey(value)

        raise ValueError("引数として与えられたキーが、定義したホットキーリストに含まれていません")

    def __isNumberString(self, value: str) -> bool:
        if not type(value) == str: raise TypeError(self.ERR_MSG_TYPEERROR_STR)
        return True if value in self.number else False

    def __isAlphabet(self, value: str) -> bool:
        if not type(value) == str: raise TypeError(self.ERR_MSG_TYPEERROR_STR)
        return True if value in self.alphabet else False

    def __isSymbol(self, value: str) -> bool:
        if not type(value) == str: raise TypeError(self.ERR_MSG_TYPEERROR_STR)
        return True if value in self.symbol else False

    def __isControl(self, value: str) -> bool:
        if not type(value) == str: raise TypeError(self.ERR_MSG_TYPEERROR_STR)
        return True if value in self.control else False
    
    def __convertToAskkey(self, value: str) -> int:
        """文字列リテラルをasciiコードに変換"""
        value_upper = str.upper(value)
        return ord(value_upper)

    def __convertToAskkey_individual(self, value: str) -> int:
        """__convertToAskkeyメソッドにキーの文字列を渡して
        キーコードへ変換できなかったキーはこちらで個別に定義する"""
        value_lower = str.lower(value) # 大文字小文字を区別させない
        key_dict = {
            "_": 226,
            "-": 189,
            ",": 188,
            ";": 187,
            ":": 186,
            ".": 190,
            "[": 219,
            "]": 221,
            "@": 192,
            "/": 191,
            "\\": 220,
            "^": 222,
        }
        return key_dict[value_lower]
        
    def __convertToWxPythonKey(self, value: str) -> int:
        value_lower = str.lower(value) # 大文字小文字を区別させない
        key_dict = {
            "left": wx.WXK_LEFT,
            "right": wx.WXK_RIGHT,
            "down": wx.WXK_DOWN,
            "up": wx.WXK_UP,
            "space": wx.WXK_SPACE,
            "tab": wx.WXK_TAB,
        }
        return key_dict[value_lower]
