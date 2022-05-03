# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from settinggui import Ui_Setting

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class RootGUI():
    def __init__(self):
        root = QApplication(sys.argv)
        self.root = root

    def start(self, GUIClass):
        gui_ = GUIClass()
        gui_.visible()
        sys.exit(self.root.exec_()) # MEMO: これを記述しておかないとモーダル状態にならない(すぐ消えてしまう)
        
    def stop(self):
        sys.exit(self.root.exec_())


class AbstractGui:
    """個別uiイベント登録用のメソッド"""
    def visible(self):
        self.show()
    
    def hidden(self):
        self.hide()

    def quit(self):
        self.close()


class SettingGUI(AbstractGui, QDialog):
    def __init__(self, root, parent=None):
        super(SettingGUI, self).__init__(parent)
        self.root = root
        self.ui = Ui_Setting() # ここに表示させるguiを定義
        
        # QtDesignerで作成した全体のui(.uiから.pyへの変換ファイル)のsetup
        self.ui.setupUi(self)
    
    # =========================================================================
    # QtDesigner作成後に追加で設定するセットアップを定義
    # =========================================================================
    # -------------------------------------------------------------------------
    # PushButton
    # -------------------------------------------------------------------------
    def setupPushButton(self, list_):
        """イベント登録(シグナル/スロット)"""
        self.__bindOnClick_PushButton_FromList(list_)

    def __bindOnClick_PushButton_FromList(self, list_):
        for i in range(0, len(list_)):
            self.__bindOnClick_PushButton(list_[i][0], list_[i][1])
    
    def __bindOnClick_PushButton(self, push_button, on_event_function):
        push_button.clicked.connect(lambda: on_event_function())
    # -------------------------------------------------------------------------
    # ComboBox
    # -------------------------------------------------------------------------
    def setupComboBox(self, list_):
        self.__addItems_ComboBox_FromList(list_)

    def __addItems_ComboBox_FromList(self, list_):
        """example.
        combobox_item = (self.gui.ui.comboBox_Hotkey_WindowLeft, json_dict_combobox)
        """
        for i in range(0, len(list_)):
            self.__addItems_ComboBox(list_[i][0], list_[i][1])
    
    def __addItems_ComboBox(self, combo_box, list_):
        combo_box.addItems(list_)
    # -------------------------------------------------------------------------
    # CheckBox
    # -------------------------------------------------------------------------
    def setupCheckBox(self, list_):
        self.__checked_CheckBox_FromList(list_)

    def __checked_CheckBox_FromList(self, list_):
        """example.
        checkbox_item = (self.gui.ui.checkBox_windowleft_mod_ctrl, False)
        """
        for i in range(0, len(list_)):
            self.__checked_CheckBox(list_[i][0], list_[i][1])

    def __checked_CheckBox(self, check_box, b: bool):
        check_box.setChecked(b)


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

    def start(self):
        # 各タブのItemの値をJsonから書き換え
        # TODO: ここにjsonのread処理(以下、gui表示時の書き換え処理)
        self.__setupWidget()
        self.__setupTab_Size()
        self.__setupTab_Position()
        self.__setupTab_ShortcutKey()

        # gui開始(表示させる)
        self.root.start(lambda: self.gui)

    def __setupWidget(self):
        """ウィジェット全体のsetup(全タブ共通)"""
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
        self.gui.ui.spinBox_resize_max_cnt.setValue(2)
        self.gui.ui.doubleSpinBox_resize_ratio.setValue(3)
        self.gui.ui.spinBox_base_width_toleft_px.setValue(4)
        self.gui.ui.spinBox_base_width_toright_px.setValue(5)
        self.gui.ui.spinBox_adjust_width_px.setValue(6)
        self.gui.ui.checkBox_is_subtract_taskbar.setChecked(False)

    def __setupTab_Position(self):
        """位置タブのsetup"""
        self.gui.ui.spinBox_adjust_x_px.setValue(100)

    def __setupTab_ShortcutKey(self):
        """ショートカットキータブのsetup"""
        # ComboBox
        json_dict_combobox = ["uhohohohoh", "unyannyanna", "fadfaf;;", "fdadfa"]
        combobox_list = []
        # - WindowLeft
        combobox_item = (self.gui.ui.comboBox_Hotkey_WindowLeft, json_dict_combobox)
        combobox_list.append(combobox_item)
        # - WindowRight
        combobox_item = (self.gui.ui.comboBox_Hotkey_WindowRight, json_dict_combobox)
        combobox_list.append(combobox_item)
        # - setup
        self.gui.setupComboBox(combobox_list)

        # CheckBox
        checkbox_list = []
        # - WindowLeft
        checkbox_item = (self.gui.ui.checkBox_windowleft_mod_ctrl, False)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowleft_mod_shift, True)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowleft_mod_alt, False)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowleft_mod_win, True)
        checkbox_list.append(checkbox_item)
        # - WindowRight
        checkbox_item = (self.gui.ui.checkBox_windowright_mod_ctrl, False)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowright_mod_shift, True)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowright_mod_alt, False)
        checkbox_list.append(checkbox_item)
        checkbox_item = (self.gui.ui.checkBox_windowright_mod_win, True)
        checkbox_list.append(checkbox_item)
        # - setup
        self.gui.setupCheckBox(checkbox_list)


# -------------------------------------------------------------------------
# Local functions
# -------------------------------------------------------------------------
if __name__ == '__main__':
    gui_service = GuiService()
    gui_service.start()