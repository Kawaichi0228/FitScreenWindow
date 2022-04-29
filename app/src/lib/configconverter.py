# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from src.lib.keylist import ModifireKey, Hotkey

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class ConfigConverter:
    """Config.pyに格納された各ホットキーの値を、
    wxPython対応のキーコードへ変換するクラス"""
    def convertHotkeyConfigToKeycode(self, HotkeyWindowLeftRight) -> dict:
        """
        修飾キーの組み合わせと単体ホットキーのキーコードをdictとして返す
        MEMO: Configクラスを用いたダックタイピングを使用
        """
        # 修飾キー(configのValueが 1 だった場合に変換して格納する)
        modk = ModifireKey()
        if HotkeyWindowLeftRight.mod_ctrl == 1: modk.add(modk.CTRLKEY)
        if HotkeyWindowLeftRight.mod_shift == 1: modk.add(modk.SHIFTKEY)
        if HotkeyWindowLeftRight.mod_alt == 1: modk.add(modk.ALTKEY)
        if HotkeyWindowLeftRight.mod_win == 1: modk.add(modk.WINKEY)
        mod_combination = modk.getCombinationKeycode()
        
        # ホットキー
        hk = Hotkey()
        hotkey = hk.getKeycode(HotkeyWindowLeftRight.hotkey)

        return {"mod_combination": mod_combination, "hotkey": hotkey}
        
