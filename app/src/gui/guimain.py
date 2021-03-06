# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from src.gui.configgui import Ui_ConfigGUI

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class RootGui():
    def __init__(self) -> None:
        root = QApplication(sys.argv)
        self.root = root

    def start(self, GUIClass) -> None:
        gui_ = GUIClass()
        gui_.visible()

        # /*
        # MEMO: 恐らくこのGUI以外のスレッド(ex.グローバルホットキー, タスクトレイ等)が
        # 既に走っている場合は、GUIウィンドウが消えずに残ってくれたためコメントアウトした。※未検証
        #sys.exit(self.root.exec_()) # MEMO: これを記述しておかないとモーダル状態にならない(すぐ消えてしまう)
        # */
        
    def stop(self) -> None:
        sys.exit(self.root.exec_())


class UtilGui:
    """個別uiイベント登録用のメソッド"""
    def visible(self) -> None:
        self.show()
    
    def hidden(self) -> None:
        self.hide()

    def quit(self) -> None:
        self.close()


class ConfigGui(UtilGui, QDialog):

    def __init__(self, root, parent=None) -> None:
        super(ConfigGui, self).__init__(parent)
        self.root = root
        self.ui = Ui_ConfigGUI() # ここに表示させるguiを定義

        # QtDesignerで作成した全体のui(.uiから.pyへの変換ファイル)のsetup
        self.ui.setupUi(self)

        self.widgets = self.ui

    # [OverRige] Qtイベントメソッドをオーバーライド
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    # ウィンドウ全体を動かせるメソッド
    def moveWindow(self, e):
        # 左クリック時のみにウィンドウを動かす
        if e.buttons() == Qt.LeftButton:
            self.move(self.pos() + e.globalPos() - self.clickPosition)
            self.clickPosition = e.globalPos()
            e.accept()

    # =========================================================================
    # QtDesigner作成後に追加で設定するセットアップを定義
    # =========================================================================
    # -------------------------------------------------------------------------
    # Window
    # -------------------------------------------------------------------------
    def setupWindow(self) -> None:
        """フレームレス"""
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
    # -------------------------------------------------------------------------
    # PushButton
    # -------------------------------------------------------------------------
    # MEMO:
    # list_[i][0]: pushButton(Object)
    # list_[i][1]: bindEventFunction(Object)
    # list_[i][2]: isSetFocus(bool)
    def setupPushButton(self, list_) -> None:
        self.__setFocus_PushButton_FromList(list_)
        self.__bindOnClick_PushButton_FromList(list_)
    
    def __setFocus_PushButton_FromList(self, list_) -> None:
        for i in range(0, len(list_)):
            if list_[i][2]:
                self.__setFocus_PushButton(list_[i][0])

    def __bindOnClick_PushButton_FromList(self, list_) -> None:
        for i in range(0, len(list_)):
            self.__bindOnClick_PushButton(list_[i][0], list_[i][1])
            
    def __setFocus_PushButton(self, push_button) -> None:
        push_button.setFocus()
    
    def __bindOnClick_PushButton(self, push_button, on_event_function) -> None:
        """イベント登録(シグナル/スロット)"""
        push_button.clicked.connect(lambda: on_event_function())
    # -------------------------------------------------------------------------
    # ComboBox
    # -------------------------------------------------------------------------
    # MEMO:
    # list_[i][0]: self.gui.ui.comboBox_Hotkey_WindowLeft || Right
    # list_[i][1]: key_list
    # list_[i][2]: Config.HotkeyWindowLeft || Right.hotkey
    # example.
    # <combobox_item = (self.gui.ui.comboBox_Hotkey_WindowLeft, key_list, Config.HotkeyWindowLeft.hotkey)>
    def setupComboBox(self, list_) -> None:
        self.__clearItem_ComboBox_FromList(list_)
        self.__addItems_ComboBox_FromList(list_)
        self.__setItem_ComboBox_FromList(list_)

    def __clearItem_ComboBox_FromList(self, list_) -> None:
        for i in range(0, len(list_)):
            self.__clearItem_ComboBox(list_[i][0])

    def __addItems_ComboBox_FromList(self, list_) -> None:
        for i in range(0, len(list_)):
            self.__addItems_ComboBox(list_[i][0], list_[i][1])

    def __setItem_ComboBox_FromList(self, list_) -> None:
        for i in range(0, len(list_)):
            self.__setItem_ComboBox(list_[i][0], list_[i][2])

    def __clearItem_ComboBox(self, combo_box) -> None:
        """コンボボックスのリストアイテムを全て消去する"""
        combo_box.clear()
    
    def __addItems_ComboBox(self, combo_box, list_) -> None:
        """コンボボックスにリストアイテムを追加する"""
        combo_box.addItems(list_)

    def __setItem_ComboBox(self, combo_box, select_itemtext) -> None:
        """指定したTextのItemをコンボボックスの初期選択とする"""
        combo_box.setCurrentIndex(
            combo_box.findText(select_itemtext)
        )
    # -------------------------------------------------------------------------
    # CheckBox
    # -------------------------------------------------------------------------
    def setupCheckBox(self, list_) -> None:
        self.__checked_CheckBox_FromList(list_)

    def __checked_CheckBox_FromList(self, list_) -> None:
        """example.
        checkbox_item = (self.gui.ui.checkBox_windowleft_mod_ctrl, False)
        """
        for i in range(0, len(list_)):
            self.__checked_CheckBox(list_[i][0], list_[i][1])

    def __checked_CheckBox(self, check_box, b: bool) -> None:
        check_box.setChecked(b)