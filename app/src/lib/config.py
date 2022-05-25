# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from logging import getLogger
from src.lib.logger import *
logger = getLogger("Log")

from src.lib.keylist import ModifireKey, Hotkey
from src.lib.jsoncontroller import JsonController
from src.gui.guimain import RootGui, ConfigGui
from src.lib.dialog import Dialog, ErrorDialog
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
        resize_add_width_px: float # リサイズごと(カウンタと連動)の拡大倍率(基準サイズから×n倍するか)
        base_width_toleft_px: int # 初期リサイズ時のウィンドウサイズ
        base_width_toright_px: int # 初期リサイズ時のウィンドウサイズ
        adjust_width_px: int # なぜか完全に画面にぴったりフィットしないため、その調整用(恐らくウィンドウの枠のサイズ？)
        is_subtract_taskbar: bool # タスクバーのサイズを差し引くか
        is_reverse_direction_windowleft: bool # 逆方向へ拡大させるか
        is_reverse_direction_windowright: bool # 逆方向へ拡大させるか

    @dataclass(frozen=False)
    class Position:
        """PositionCalclator専用のパラメータオブジェクト"""
        adjust_x_px: int # なぜか完全に画面にぴったりフィットしないため、その調整用(恐らくウィンドウの角丸枠のサイズ？)

    @dataclass(frozen=False)
    class HotkeyWindowLeft:
        mod_ctrl: bool
        mod_shift: bool
        mod_alt: bool
        mod_win: bool
        hotkey: str

    @dataclass(frozen=False)
    class HotkeyWindowRight:
        mod_ctrl: bool
        mod_shift: bool
        mod_alt: bool
        mod_win: bool
        hotkey: str
        
    @staticmethod
    def validate() -> dict:
        try:
            # 全プロパティをここに記述する
            Config.Size.resize_max_cnt
            Config.Size.resize_add_width_px
            Config.Size.base_width_toleft_px
            Config.Size.base_width_toright_px
            Config.Size.adjust_width_px
            Config.Size.is_subtract_taskbar
            Config.Size.is_reverse_direction_windowleft
            Config.Size.is_reverse_direction_windowright
            Config.Position.adjust_x_px
            Config.HotkeyWindowLeft.mod_ctrl
            Config.HotkeyWindowLeft.mod_shift
            Config.HotkeyWindowLeft.mod_alt
            Config.HotkeyWindowLeft.mod_win
            Config.HotkeyWindowLeft.hotkey
            Config.HotkeyWindowRight.mod_ctrl
            Config.HotkeyWindowRight.mod_shift
            Config.HotkeyWindowRight.mod_alt
            Config.HotkeyWindowRight.mod_win
            Config.HotkeyWindowRight.hotkey

        except AttributeError as e:
            raise AttributeError( \
                "定義されていないプロパティが存在します。全てのプロパティを定義してください。\n" \
                f"{e.args[0]}"
            )
        return

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
        # 修飾キー(configのValueが True だった場合に変換して格納する)
        modk = ModifireKey()
        if HotkeyWindowLeftRight.mod_ctrl: modk.addCombination(modk.CTRLKEY)
        if HotkeyWindowLeftRight.mod_shift: modk.addCombination(modk.SHIFTKEY)
        if HotkeyWindowLeftRight.mod_alt: modk.addCombination(modk.ALTKEY)
        if HotkeyWindowLeftRight.mod_win: modk.addCombination(modk.WINKEY)
        mod_combination = modk.getCombinationKeycode()
        
        # ホットキー
        hk = Hotkey()
        hotkey = hk.getKeycode(HotkeyWindowLeftRight.hotkey)

        return {"mod_combination": mod_combination, "hotkey": hotkey}


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
# Configクラス(このファイル=Config.py)の各プロパティに値をセットするためのClass
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
class IConfigSet(ABC):
    @abstractmethod
    def _setupConfigPython(self) -> None: pass
    
    def setupConfigPython(self) -> None:
        self._setupConfigPython()
        Config.validate() # 全てのプロパティが定義されているか確認
        logger.info("config.pyへ変数値の書き換えが完了しました")


class ConfigDefault(IConfigSet):
    """初期値設定用"""
    def _setupConfigPython(self) -> None:
        Config.Size.resize_max_cnt = 4
        Config.Size.resize_add_width_px = 100
        Config.Size.base_width_toleft_px = 700
        Config.Size.base_width_toright_px = 700
        Config.Size.adjust_width_px = 20
        Config.Size.is_subtract_taskbar = True
        Config.Size.is_reverse_direction_windowleft = False
        Config.Size.is_reverse_direction_windowright = False
        Config.Position.adjust_x_px = 10
        Config.HotkeyWindowLeft.mod_ctrl = False
        Config.HotkeyWindowLeft.mod_shift = True
        Config.HotkeyWindowLeft.mod_alt = True
        Config.HotkeyWindowLeft.mod_win = False
        Config.HotkeyWindowLeft.hotkey = "Left"
        Config.HotkeyWindowRight.mod_ctrl = False
        Config.HotkeyWindowRight.mod_shift = True
        Config.HotkeyWindowRight.mod_alt = True
        Config.HotkeyWindowRight.mod_win = False
        Config.HotkeyWindowRight.hotkey = "Right"


class ConfigJsonRepository(IConfigSet):
    """※Jsonの値を参照したいときは、このクラスのsetupメソッドでConfigクラスを書き換えて、
    それを参照すること(直接このクラスの永続化されたJson値を参照しない)"""
    def __init__(self) -> None:
        # jsonを読み込み、dictionaryとしてインスタンス変数化(永続化)
        jc = JsonController(CONFIG_JSON_PATH)
        self.__jc = jc
        json_object = self.__read()
        json_dict = self.__jc.getDictionary(json_object)
        self.json_dict = json_dict

    def _setupConfigPython(self) -> None:
        """config.pyをjsonで読みとった値で書き換え"""
        Config.Size.resize_max_cnt = self.json_dict["size"]["resize_max_cnt"]
        Config.Size.resize_add_width_px = self.json_dict["size"]["resize_add_width_px"]
        Config.Size.base_width_toleft_px = self.json_dict["size"]["base_width_toleft_px"]
        Config.Size.base_width_toright_px = self.json_dict["size"]["base_width_toright_px"]
        Config.Size.adjust_width_px = self.json_dict["size"]["adjust_width_px"]
        Config.Size.is_subtract_taskbar = self.json_dict["size"]["is_subtract_taskbar"]
        Config.Size.is_reverse_direction_windowleft = self.json_dict["size"]["is_reverse_direction_windowleft"]
        Config.Size.is_reverse_direction_windowright = self.json_dict["size"]["is_reverse_direction_windowright"]
        Config.Position.adjust_x_px = self.json_dict["position"]["adjust_x_px"]
        Config.HotkeyWindowLeft.mod_ctrl = self.json_dict["hotkey_windowleft"]["mod_ctrl"]
        Config.HotkeyWindowLeft.mod_shift = self.json_dict["hotkey_windowleft"]["mod_shift"]
        Config.HotkeyWindowLeft.mod_alt = self.json_dict["hotkey_windowleft"]["mod_alt"]
        Config.HotkeyWindowLeft.mod_win = self.json_dict["hotkey_windowleft"]["mod_win"]
        Config.HotkeyWindowLeft.hotkey = self.json_dict["hotkey_windowleft"]["hotkey"]
        Config.HotkeyWindowRight.mod_ctrl = self.json_dict["hotkey_windowright"]["mod_ctrl"]
        Config.HotkeyWindowRight.mod_shift = self.json_dict["hotkey_windowright"]["mod_shift"]
        Config.HotkeyWindowRight.mod_alt = self.json_dict["hotkey_windowright"]["mod_alt"]
        Config.HotkeyWindowRight.mod_win = self.json_dict["hotkey_windowright"]["mod_win"]
        Config.HotkeyWindowRight.hotkey = self.json_dict["hotkey_windowright"]["hotkey"]

    def setupConfigJsonDictionary(self) -> None:
        try:
            self.json_dict["size"]["resize_max_cnt"] = Config.Size.resize_max_cnt
            self.json_dict["size"]["resize_add_width_px"] = Config.Size.resize_add_width_px
            self.json_dict["size"]["base_width_toleft_px"] = Config.Size.base_width_toleft_px
            self.json_dict["size"]["base_width_toright_px"] = Config.Size.base_width_toright_px
            self.json_dict["size"]["adjust_width_px"] = Config.Size.adjust_width_px
            self.json_dict["size"]["is_subtract_taskbar"] = Config.Size.is_subtract_taskbar
            self.json_dict["size"]["is_reverse_direction_windowleft"] = Config.Size.is_reverse_direction_windowleft
            self.json_dict["size"]["is_reverse_direction_windowright"] = Config.Size.is_reverse_direction_windowright
            self.json_dict["position"]["adjust_x_px"] = Config.Position.adjust_x_px
            self.json_dict["hotkey_windowleft"]["mod_ctrl"] = Config.HotkeyWindowLeft.mod_ctrl
            self.json_dict["hotkey_windowleft"]["mod_shift"] = Config.HotkeyWindowLeft.mod_shift
            self.json_dict["hotkey_windowleft"]["mod_alt"] = Config.HotkeyWindowLeft.mod_alt
            self.json_dict["hotkey_windowleft"]["mod_win"] = Config.HotkeyWindowLeft.mod_win
            self.json_dict["hotkey_windowleft"]["hotkey"] = Config.HotkeyWindowLeft.hotkey
            self.json_dict["hotkey_windowright"]["mod_ctrl"] = Config.HotkeyWindowRight.mod_ctrl
            self.json_dict["hotkey_windowright"]["mod_shift"] = Config.HotkeyWindowRight.mod_shift
            self.json_dict["hotkey_windowright"]["mod_alt"] = Config.HotkeyWindowRight.mod_alt
            self.json_dict["hotkey_windowright"]["mod_win"] = Config.HotkeyWindowRight.mod_win
            self.json_dict["hotkey_windowright"]["hotkey"] = Config.HotkeyWindowRight.hotkey
        except AttributeError:
            raise AttributeError("代入エラー: 代入対象のConfigの値に、Blank値が混入しています")

    def __read(self) -> object:
        # jsonファイルを読み込む
        try:
            json_obj = self.__jc.read()
            logger.info("config.jsonの読込が正常に完了しました")
        except FileNotFoundError:
            ErrorDialog().showFileNotFound("config.json")
            ErrorHandling().quitApp()
        return json_obj

    def save(self) -> None:
        self.__jc.save(self.json_dict)


class ConfigGuiService(IConfigSet):
    """
    QtDesigner作成後に追加で設定する、個別のuiのsetup
        MEMO: .uiから.pyへ変換したpythonファイルから、このクラスの各setupメソッドへ
        外部定義したいコードをコピペすればOK
        (ただし、追加で ".ui" を付けること <ex. self.ui.comboBox...>)
    """
    def __init__(self, GlobalHotkeyService):
        root = RootGui()
        self.root = root

        gui = ConfigGui(root)
        self.gui = gui

        # ウィジェットの全体設定(インスタンス化時に1度のみ行う)
        self.__setupWidget()

        # config.jsonから値を読み取り、jsonのValueが格納されたDictを取得
        json_repository = ConfigJsonRepository()
        # config.pyの各データクラスの値を上書きする
        json_repository.setupConfigPython()

        # 既に開始されているGlobalHotkeyスレッドをこのクラスから操作するために、
        # GlobalHotkeyServiceのインスタンスを引数経由で受け取る
        # (ApplicationServiceで既に生成されているインスタンスを渡すため、
        # カッコをつけていない(インスタンス化していない)
        g_service = GlobalHotkeyService 
        self.g_service = g_service

    def _setupConfigPython(self) -> None:
        Config.Size.resize_max_cnt = self.gui.ui.lineEdit_resize_max_cnt.displayText()
        Config.Size.resize_add_width_px = self.gui.ui.lineEdit_resize_add_width_px.displayText()
        Config.Size.base_width_toleft_px = self.gui.ui.lineEdit_base_width_toleft_px.displayText()
        Config.Size.base_width_toright_px = self.gui.ui.lineEdit_base_width_toright_px.displayText()
        Config.Size.adjust_width_px = self.gui.ui.lineEdit_adjust_width_px.displayText()
        Config.Size.is_subtract_taskbar = self.gui.ui.checkBox_is_subtract_taskbar.isChecked()
        Config.Size.is_reverse_direction_windowleft = self.gui.ui.checkBox_is_reverse_direction_windowleft.isChecked()
        Config.Size.is_reverse_direction_windowright = self.gui.ui.checkBox_is_reverse_direction_windowright.isChecked()
        Config.Position.adjust_x_px = self.gui.ui.lineEdit_adjust_x_px.displayText()
        Config.HotkeyWindowLeft.mod_ctrl = self.gui.ui.checkBox_windowleft_mod_ctrl.isChecked()
        Config.HotkeyWindowLeft.mod_shift = self.gui.ui.checkBox_windowleft_mod_shift.isChecked()
        Config.HotkeyWindowLeft.mod_alt = self.gui.ui.checkBox_windowleft_mod_alt.isChecked()
        Config.HotkeyWindowLeft.mod_win = self.gui.ui.checkBox_windowleft_mod_win.isChecked()
        Config.HotkeyWindowLeft.hotkey = self.gui.ui.comboBox_Hotkey_WindowLeft.currentText()
        Config.HotkeyWindowRight.mod_ctrl = self.gui.ui.checkBox_windowright_mod_ctrl.isChecked()
        Config.HotkeyWindowRight.mod_shift = self.gui.ui.checkBox_windowright_mod_shift.isChecked()
        Config.HotkeyWindowRight.mod_alt = self.gui.ui.checkBox_windowright_mod_alt.isChecked()
        Config.HotkeyWindowRight.mod_win = self.gui.ui.checkBox_windowright_mod_win.isChecked()
        Config.HotkeyWindowRight.hotkey = self.gui.ui.comboBox_Hotkey_WindowRight.currentText()

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def start(self):
        # GUIの表示開始時に、グローバルホットキーのスレッドを停止(GUI操作中にホットキー操作できないようにするため)
        self.g_service.stopThread()
        logger.info("GUIの値からconfig.jsonを保存しました")

        # --- 各タブのItemの値をJsonから書き換え ---
        self.__setupTab_Size()
        self.__setupTab_Position()
        self.__setupTab_ShortcutKey()

        # gui開始(表示させる)
        self.root.start(lambda: self.gui)

    def stop(self) -> None:
        # グローバルホットキーのスレッドを再開(GUIで設定した値で再度バインドされる)
        self.g_service.startThread()

        # GUIスレッド終了
        self.gui.quit()

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def __setupWidget(self):
        """ウィジェット全体のsetup(全タブ共通)"""
        # Window
        self.gui.setupWindow_CloseButtonOnly()

        # PushButton
        pushbutton_list = []
        # - OKButton
        set_focus = True # 最初の選択状態にしておく
        pushbutton_item = (self.gui.ui.pushButton_saveandexit, self.__onClickEvent_pushButton_ok, set_focus)
        pushbutton_list.append(pushbutton_item)
        # - CancelButton
        set_focus = False
        pushbutton_item = (self.gui.ui.pushButton_cancel, self.__onClickEvent_pushButton_cancel, set_focus)
        pushbutton_list.append(pushbutton_item)
        # - InitializeSettingButton
        set_focus = False
        pushbutton_item = (self.gui.ui.pushButton_initialize_setting, self.__onClickEvent_pushButton_initialize_setting, set_focus)
        pushbutton_list.append(pushbutton_item)
        # - setup
        self.gui.setupPushButton(pushbutton_list)

    def __onClickEvent_pushButton_ok(self) -> None:
        # Config.pyのクラスへ値をセット
        self._setupConfigPython()

        # JsonへConfig.pyに格納された値を保存
        self.__readAndSaveJson()
        logger.info("GUIの値からconfig.jsonを保存しました")

        # GUIスレッド終了
        self.stop()

    def __onClickEvent_pushButton_cancel(self) -> None:
        # GUIスレッド終了
        self.stop()
    
    def __onClickEvent_pushButton_initialize_setting(self) -> None:
        dialog = Dialog()
        value = "設定を全て初期化します。よろしいですか？"
        user_input = dialog.showOKCancelnfomation(title="Fit Screen Window - 確認", value=value, is_cancel_default=True)

        if user_input: # OKボタン押下時
            # Configクラスの全プロパティを指定した初期値にセット
            config_default = ConfigDefault()
            config_default.setupConfigPython()

            # JsonへConfig.pyに格納された値を保存
            self.__readAndSaveJson()
            logger.info("初期値設定用クラスの値からconfig.jsonを保存しました")
            
            # GUIスレッド終了
            self.stop()

    def __readAndSaveJson(self) -> None:
        # GUIの各値を取得し、Config.pyのクラス値をインスタンスのJsonDictionaryへいったん書き換える
        json = ConfigJsonRepository()
        json.setupConfigJsonDictionary()

        # インスタンスのJsonDictionaryの値からJsonへ書き込み保存
        json.save()
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def __setupTab_Size(self):
        """サイズタブのsetup"""
        self.gui.ui.lineEdit_resize_max_cnt.setText(str(Config.Size.resize_max_cnt))
        self.gui.ui.lineEdit_resize_add_width_px.setText(str(Config.Size.resize_add_width_px))
        self.gui.ui.lineEdit_base_width_toleft_px.setText(str(Config.Size.base_width_toleft_px))
        self.gui.ui.lineEdit_base_width_toright_px.setText(str(Config.Size.base_width_toright_px))
        self.gui.ui.lineEdit_adjust_width_px.setText(str(Config.Size.adjust_width_px))
        self.gui.ui.checkBox_is_subtract_taskbar.setChecked(Config.Size.is_subtract_taskbar)
        self.gui.ui.checkBox_is_reverse_direction_windowleft.setChecked(Config.Size.is_reverse_direction_windowleft)
        self.gui.ui.checkBox_is_reverse_direction_windowright.setChecked(Config.Size.is_reverse_direction_windowright)

    def __setupTab_Position(self):
        """位置タブのsetup"""
        self.gui.ui.lineEdit_adjust_x_px.setText(str(Config.Position.adjust_x_px))

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