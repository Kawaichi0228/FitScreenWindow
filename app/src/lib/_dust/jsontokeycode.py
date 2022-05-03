from const import (
    JSONKEY_CTRL,
    JSONKEY_SHIFT,
    JSONKEY_ALT,
    JSONKEY_HOTKEY
)
from keycode import KeyCode

# HACK: appと同じフォルダに置いたほうが見やすいかも(Serviceクラスのように)
class JsonToKeycode:
    """jsonに格納された各ホットキーの値(文字列)から、
    wxモジュール対応のキーコードへ変換し取得するクラス"""
    def convert(self, json_dict) -> dict:
        """修飾キーの組み合わせと単体ホットキーのキーコードをdictとして返す"""
        # 修飾キー(jsonのValueが 1 だった場合に変換して格納する)
        hk = KeyCode()
        if json_dict[JSONKEY_CTRL] == 1: hk.addModkeyCombination(hk.CTRLKEY)
        if json_dict[JSONKEY_SHIFT] == 1: hk.addModkeyCombination(hk.SHIFTKEY)
        if json_dict[JSONKEY_ALT] == 1: hk.addModkeyCombination(hk.ALTKEY)
        mod_combination = hk.getModkeyCombination()
        
        # ホットキー
        hotkey = hk.getAskkey(json_dict[JSONKEY_HOTKEY])

        return {"mod_combination": mod_combination, "hotkey": hotkey}