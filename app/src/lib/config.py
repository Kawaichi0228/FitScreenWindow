# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
# MEMO: jsonの読込失敗時等のために初期値を設定している
from dataclasses import dataclass

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
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