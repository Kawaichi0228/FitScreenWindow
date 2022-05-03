# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from dataclasses import dataclass

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class Config:
    """
    - データクラス化はクラス変数のため、全インスタンス共通のグローバル変数のように扱うことができる
    - 内部クラス化することでネストされたクラスをPrivate化することができる(外部参照不可)
    - config.jsonを使用しなくても動作させられるように、初期値をクラスに定義している
    """
    @dataclass(frozen=False) # frozen=False: セッタ可能にする
    class Size:
        """SizeCalclatorAtCounter専用のパラメータオブジェクト"""
        resize_max_cnt: int = 4 # 段階リサイズを実行できる最大回数
        resize_ratio: float = 3.5 # リサイズごと(カウンタと連動)の拡大倍率(基準サイズから×n倍するか)
        base_width_toleft_px: int = 500 # 初期リサイズ時のウィンドウサイズ
        base_width_toright_px: int = 500 # 初期リサイズ時のウィンドウサイズ
        adjust_width_px: int = 15 # なぜか完全に画面にぴったりフィットしないため、その調整用(恐らくウィンドウの枠のサイズ？)

    @dataclass(frozen=False)
    class Position:
        """PositionCalclator専用のパラメータオブジェクト"""
        adjust_x_px: int = 5 # なぜか完全に画面にぴったりフィットしないため、その調整用(恐らくウィンドウの角丸枠のサイズ？)

    @dataclass(frozen=False)
    class HotkeyWindowLeft:
        mod_ctrl: int = 1
        mod_shift: int = 1
        mod_alt: int = 0
        hotkey: str = "g"

    @dataclass(frozen=False)
    class HotkeyWindowRight:
        mod_ctrl: int = 1
        mod_shift: int = 1
        mod_alt: int = 0
        hotkey: str = "h"

class ConfigJsonToPython:
    def __init__(self, json_dict) -> None:
        self.json_dict = json_dict

    def overWriteConfig(self) -> None:
        """config.pyをjsonで読みとった値で書き換え"""
        json_size = self.json_dict["size"]
        
        Config.Size.resize_max_cnt = json_size["resize_max_cnt"]
        Config.Size.resize_ratio = json_size["resize_ratio"]
        Config.Size.base_width_toleft_px = json_size["base_width_toleft_px"]
        Config.Size.base_width_toright_px = json_size["base_width_toright_px"]
        Config.Size.adjust_width_px = json_size["adjust_width_px"]
        Config.Size.is_subtract_taskbar = json_size["is_subtract_taskbar"]
        
        json_position = self.json_dict["position"]
        Config.Position.adjust_x_px = json_position["adjust_x_px"]

        json_hotkey_windowleft = self.json_dict["hotkey_windowleft"]
        Config.HotkeyWindowLeft.mod_ctrl = json_hotkey_windowleft["mod_ctrl"]
        Config.HotkeyWindowLeft.mod_shift = json_hotkey_windowleft["mod_shift"]
        Config.HotkeyWindowLeft.mod_alt = json_hotkey_windowleft["mod_alt"]
        Config.HotkeyWindowLeft.mod_win = json_hotkey_windowleft["mod_win"]
        Config.HotkeyWindowLeft.hotkey = json_hotkey_windowleft["hotkey"]

        json_hotkey_windowright = self.json_dict["hotkey_windowright"]
        Config.HotkeyWindowRight.mod_ctrl = json_hotkey_windowright["mod_ctrl"]
        Config.HotkeyWindowRight.mod_shift = json_hotkey_windowright["mod_shift"]
        Config.HotkeyWindowRight.mod_alt = json_hotkey_windowright["mod_alt"]
        Config.HotkeyWindowRight.mod_win = json_hotkey_windowright["mod_win"]
        Config.HotkeyWindowRight.hotkey = json_hotkey_windowright["hotkey"]

