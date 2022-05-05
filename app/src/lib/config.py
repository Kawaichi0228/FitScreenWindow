# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from dataclasses import dataclass

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from src.lib.keylist import ModifireKey, Hotkey
from src.lib.jsoncontroller import JsonController
from src.gui.guimain import RootGUI, SettingGUI
from src.lib.errordialog import ErrorDialog
from src.lib.errorhandling import ErrorHandling
from src.lib.const import CONFIG_JSON_PATH

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


class ConfigJsonRepository:
    def __init__(self) -> None:
        # jsonを読み込み、dictionaryとしてインスタンス変数化(永続化)
        jc = JsonController(CONFIG_JSON_PATH)
        self.__jc = jc
        json_object = self.__read()
        json_dict = self.__jc.getDictionary(json_object)
        self.json_dict = json_dict

        # 永続化したdictionaryの各Valueをメンバ変数として参照できるように集約
        self.Size = _Size(self.json_dict)
        self.Position = _Position(self.json_dict)
        self.HotkeyWindowLeft = _HotkeyWindowLeft(self.json_dict)
        self.HotkeyWindowRight = _HotkeyWindowRight(self.json_dict)

    def __read(self) -> object:
        # jsonファイルを読み込む
        try:
            json_obj = self.__jc.read()
            assert print("メッセージ: config.jsonの読込が正常に完了しました") == None
        except FileNotFoundError:
            ErrorDialog().showFileNotFound("config.json")
            ErrorHandling().quitApp()
        return json_obj

    def setupConfigPython(self) -> None:
        """config.pyをjsonで読みとった値で書き換え"""
        Config.Size.resize_max_cnt = self.Size.resize_max_cnt
        Config.Size.resize_ratio = self.Size.resize_ratio
        Config.Size.base_width_toleft_px = self.Size.base_width_toright_px
        Config.Size.base_width_toright_px = self.Size.base_width_toright_px
        Config.Size.adjust_width_px = self.Size.adjust_width_px
        Config.Size.is_subtract_taskbar = self.Size.is_subtract_taskbar
        
        Config.Position.adjust_x_px = self.Position.adjust_x_px

        Config.HotkeyWindowLeft.mod_ctrl = self.HotkeyWindowLeft.mod_ctrl
        Config.HotkeyWindowLeft.mod_shift = self.HotkeyWindowLeft.mod_shift
        Config.HotkeyWindowLeft.mod_alt = self.HotkeyWindowLeft.mod_alt
        Config.HotkeyWindowLeft.mod_win = self.HotkeyWindowLeft.mod_win
        Config.HotkeyWindowLeft.hotkey = self.HotkeyWindowLeft.hotkey

        Config.HotkeyWindowRight.mod_ctrl = self.HotkeyWindowRight.mod_ctrl
        Config.HotkeyWindowRight.mod_shift = self.HotkeyWindowRight.mod_shift
        Config.HotkeyWindowRight.mod_alt = self.HotkeyWindowRight.mod_alt
        Config.HotkeyWindowRight.mod_win = self.HotkeyWindowRight.mod_win
        Config.HotkeyWindowRight.hotkey = self.HotkeyWindowRight.hotkey

        assert print("メッセージ: config.jsonからconfig.pyへ変数値の書き換えが完了しました") == None

class _Size:
    def __init__(self, json_dict) -> None:
        self.json_size = json_dict["size"]

        self.resize_max_cnt = self.json_size["resize_max_cnt"]
        self.resize_ratio = self.json_size["resize_ratio"]
        self.base_width_toleft_px = self.json_size["base_width_toleft_px"]
        self.base_width_toright_px = self.json_size["base_width_toright_px"]
        self.adjust_width_px = self.json_size["adjust_width_px"]
        self.is_subtract_taskbar = self.json_size["is_subtract_taskbar"]
    
class _Position:
    def __init__(self, json_dict) -> None:
        self.json_position = json_dict["position"]

        self.adjust_x_px = self.json_position["adjust_x_px"]

class _HotkeyWindowLeft:
    def __init__(self, json_dict) -> None:
        self.json_hotkey_windowleft = json_dict["hotkey_windowleft"]

        self.mod_ctrl = self.json_hotkey_windowleft["mod_ctrl"]
        self.mod_shift = self.json_hotkey_windowleft["mod_shift"]
        self.mod_alt = self.json_hotkey_windowleft["mod_alt"]
        self.mod_win = self.json_hotkey_windowleft["mod_win"]
        self.hotkey = self.json_hotkey_windowleft["hotkey"]

class _HotkeyWindowRight:
    def __init__(self, json_dict) -> None:
        self.json_hotkey_windowright = json_dict["hotkey_windowright"]

        self.mod_ctrl = self.json_hotkey_windowright["mod_ctrl"]
        self.mod_shift = self.json_hotkey_windowright["mod_shift"]
        self.mod_alt = self.json_hotkey_windowright["mod_alt"]
        self.mod_win = self.json_hotkey_windowright["mod_win"]
        self.hotkey = self.json_hotkey_windowright["hotkey"]


class GuiService:
    """
    QtDesigner作成後に追加で設定する、個別のuiのsetup
        MEMO: .uiから.pyへ変換したpythonファイルから、このクラスの各setupメソッドへ
        外部定義したいコードをコピペすればOK
        (ただし、追加で ".ui" を付けること <ex. self.ui.comboBox...>)
    """
    def __init__(self):
        root = RootGUI()
        self.root = root

        gui = SettingGUI(root)
        self.gui = gui
        
        # config.jsonから値を読み取り、jsonのValueが格納されたDictを取得
        json_repository = ConfigJsonRepository()
        # config.pyの各データクラスの値を上書きする
        json_repository.setupConfigPython()

    def start(self):
        # --- 各タブのItemの値をJsonから書き換え ---
        self.__setupWidget()
        self.__setupTab_Size()
        self.__setupTab_Position()
        self.__setupTab_ShortcutKey()

        # gui開始(表示させる)
        self.root.start(lambda: self.gui)

    def __setupWidget(self):
        """ウィジェット全体のsetup(全タブ共通)"""
        # Window
        self.gui.setupWindow_CloseButtonOnly()

        # PushButton
        pushbutton_list = []
        # - OKButton
        pushbutton_item = (self.gui.ui.pustButton_ok, self.gui.quit) # TODO: quitの前に、jsonのread -> 書き換え処理を入れた関数へ変更する
        pushbutton_list.append(pushbutton_item)
        # - CancelButton
        pushbutton_item = (self.gui.ui.pustButton_cancel, self.gui.quit)
        pushbutton_list.append(pushbutton_item)
        # - setup
        self.gui.setupPushButton(pushbutton_list)

    def __setupTab_Size(self):
        """サイズタブのsetup"""
        self.gui.ui.spinBox_resize_max_cnt.setValue(Config.Size.resize_max_cnt)
        self.gui.ui.doubleSpinBox_resize_ratio.setValue(Config.Size.resize_ratio)
        self.gui.ui.spinBox_base_width_toleft_px.setValue(Config.Size.base_width_toleft_px)
        self.gui.ui.spinBox_base_width_toright_px.setValue(Config.Size.base_width_toright_px)
        self.gui.ui.spinBox_adjust_width_px.setValue(Config.Size.adjust_width_px)
        self.gui.ui.checkBox_is_subtract_taskbar.setChecked(Config.Size.is_subtract_taskbar)

    def __setupTab_Position(self):
        """位置タブのsetup"""
        self.gui.ui.spinBox_adjust_x_px.setValue(Config.Position.adjust_x_px)

    def __setupTab_ShortcutKey(self):
        """ショートカットキータブのsetup"""
        # ComboBox
        hk = Hotkey()
        key_list = hk.getKeyList()
        combobox_list = []
        # - WindowLeft
        combobox_item = (self.gui.ui.comboBox_Hotkey_WindowLeft, key_list, Config.HotkeyWindowLeft.hotkey)
        combobox_list.append(combobox_item)
        # - WindowRight
        combobox_item = (self.gui.ui.comboBox_Hotkey_WindowRight, key_list, Config.HotkeyWindowRight.hotkey)
        combobox_list.append(combobox_item)
        # - setup
        self.gui.setupComboBox(combobox_list)

        # CheckBox
        checkbox_list = []
        # - WindowLeft
        checkbox_item = (self.gui.ui.checkBox_windowleft_mod_ctrl,Config.HotkeyWindowLeft.mod_ctrl)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowleft_mod_shift, Config.HotkeyWindowLeft.mod_shift)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowleft_mod_alt, Config.HotkeyWindowLeft.mod_alt)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowleft_mod_win, Config.HotkeyWindowLeft.mod_win)
        checkbox_list.append(checkbox_item)
        # - WindowRight
        checkbox_item = (self.gui.ui.checkBox_windowright_mod_ctrl, Config.HotkeyWindowRight.mod_ctrl)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowright_mod_shift, Config.HotkeyWindowRight.mod_shift)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowright_mod_alt, Config.HotkeyWindowRight.mod_alt)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowright_mod_win, Config.HotkeyWindowRight.mod_win)
        checkbox_list.append(checkbox_item)
        # - setup
        self.gui.setupCheckBox(checkbox_list)