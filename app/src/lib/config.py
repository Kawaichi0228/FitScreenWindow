# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from dataclasses import dataclass

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from src.lib.keylist import ModifireKey, Hotkey
from src.lib.jsoncontroller import JsonController

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class Config:
    # MEMO: 各ConfigのValidate(数値範囲制限)は今のところGUI作成ツールで設定している(このクラスでは定義していない)
    """
    - データクラス化はクラス変数のため、全インスタンス共通のグローバル変数のように扱うことができる
    - 内部クラス化することでネストされたクラスをPrivate化することができる(外部参照不可)
    """
    @dataclass(frozen=False) # frozen=False: セッタ可能にする
    class Size:
        """SizeCalclatorAtCounter専用のパラメータオブジェクト"""
        resize_max_cnt: int # 段階リサイズを実行できる最大回数
        resize_ratio: float # リサイズごと(カウンタと連動)の拡大倍率(基準サイズから×n倍するか)
        base_width_toleft_px: int # 初期リサイズ時のウィンドウサイズ
        base_width_toright_px: int # 初期リサイズ時のウィンドウサイズ
        adjust_width_px: int # なぜか完全に画面にぴったりフィットしないため、その調整用(恐らくウィンドウの枠のサイズ？)

    @dataclass(frozen=False)
    class Position:
        """PositionCalclator専用のパラメータオブジェクト"""
        adjust_x_px: int # なぜか完全に画面にぴったりフィットしないため、その調整用(恐らくウィンドウの角丸枠のサイズ？)

    @dataclass(frozen=False)
    class HotkeyWindowLeft:
        mod_ctrl: int # bool 1 or 0
        mod_shift: int # bool 1 or 0
        mod_alt: int # bool 1 or 0
        hotkey: str

    @dataclass(frozen=False)
    class HotkeyWindowRight:
        mod_ctrl: int # bool 1 or 0
        mod_shift: int # bool 1 or 0
        mod_alt: int # bool 1 or 0
        hotkey: str

    @staticmethod
    def getKeycodeforHotkeyWindowLeft() -> dict:
        return Config.__convertHotkeyWindowToKeycode(Config.HotkeyWindowLeft)

    @staticmethod
    def getKeycodeforHotkeyWindowRight() -> dict:
        return Config.__convertHotkeyWindowToKeycode(Config.HotkeyWindowRight)

    @staticmethod
    def __convertHotkeyWindowToKeycode(HotkeyWindowLeftRight) -> dict:
        """
        Config.pyに格納された各ホットキーの値を、
        wxPython対応のキーコードへ変換する
        return:
            修飾キーの組み合わせと単体ホットキーのキーコードをdictとして返す
        prm:
            HotkeyWindowLeftRight: クラスの HotkeyWindowLeft または HotkeyWindowRightを渡す
        other:
            Configクラスを用いたダックタイピングを使用
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


class ConfigJsonToPython:
    def __init__(self, json_dict) -> None:
        self.json_dict = json_dict

    def setupConfig(self) -> None:
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


class ConfigJsonRepository:
    def __init__(self, json_path) -> None:
        # jsonを読み込み、dictionaryとしてインスタンス変数化(永続化)
        jc = JsonController(json_path)
        self.jc = jc
        json_object = self.jc.read()
        json_dict = self.jc.getDictionary(json_object)
        self.json_dict = json_dict

        # 永続化したdictionaryの各Valueをメンバ変数として参照できるように集約
        self.Size = _Size(self.json_dict)
        self.Position = _Position(self.json_dict)
        self.HotkeyWindowLeft = _HotkeyWindowLeft(self.json_dict)
        self.HotkeyWindowRight = _HotkeyWindowRight(self.json_dict)

class _Size:
    def __init__(self, json_dict) -> None:
        self.json_dict = json_dict
        json_size = self.json_dict["size"]

        self.resize_max_cnt = json_size["resize_max_cnt"]
        self.resize_ratio = json_size["resize_ratio"]
        self.base_width_toleft_px = json_size["base_width_toleft_px"]
        self.base_width_toright_px = json_size["base_width_toright_px"]
        self.adjust_width_px = json_size["adjust_width_px"]
        self.is_subtract_taskbar = json_size["is_subtract_taskbar"]
    
class _Position:
    def __init__(self, json_dict) -> None:
        self.json_dict = json_dict
        json_position = self.json_dict["position"]

        self.adjust_x_px = json_position["adjust_x_px"]

class _HotkeyWindowLeft:
    def __init__(self, json_dict) -> None:
        self.json_dict = json_dict
        json_hotkey_windowleft = self.json_dict["hotkey_windowleft"]

        self.mod_ctrl = json_hotkey_windowleft["mod_ctrl"]
        self.mod_shift = json_hotkey_windowleft["mod_shift"]
        self.mod_alt = json_hotkey_windowleft["mod_alt"]
        self.mod_win = json_hotkey_windowleft["mod_win"]
        self.hotkey = json_hotkey_windowleft["hotkey"]

class _HotkeyWindowRight:
    def __init__(self, json_dict) -> None:
        self.json_dict = json_dict
        self.hotkey_windowright = json_hotkey_windowright = self.json_dict["hotkey_windowright"]

        self.mod_ctrl = json_hotkey_windowright["mod_ctrl"]
        self.mod_shift = json_hotkey_windowright["mod_shift"]
        self.mod_alt = json_hotkey_windowright["mod_alt"]
        self.mod_win = json_hotkey_windowright["mod_win"]
        self.hotkey = json_hotkey_windowright["hotkey"]

