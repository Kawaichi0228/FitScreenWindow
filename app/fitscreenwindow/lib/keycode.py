import wx


class KeyCode:
    """キーコード参考:http://faq.creasus.net/04/0131/CharCode.html"""
    def __init__(self) -> None:
        self.mod_list = []
        self.CTRLKEY = wx.MOD_CONTROL
        self.SHIFTKEY = wx.MOD_SHIFT
        self.ALTKEY = wx.MOD_ALT

    def addModkeyCombination(self, modkey) -> None:
        self.mod_list.append(modkey)

    def getModkeyCombination(self) -> int:
        """修飾キーの組み合わせをintとして返す"""
        join_mod = 0
        for mod in self.mod_list:
            join_mod += mod

        mod_combination = join_mod
        return mod_combination

    # TODO: SpaceやLeft,Rightなど一部のキーが正しく変換されない(違うコードになってしまう)
    def getAskkey(self, keystr) -> str:
        """文字列リテラルをasciiコードに変換"""
        keystr_upper = str.upper(keystr)
        return ord(keystr_upper)
