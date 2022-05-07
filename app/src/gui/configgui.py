# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configgui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from src.gui import resource_rc

class Ui_Config(object):
    def setupUi(self, Config):
        if not Config.objectName():
            Config.setObjectName(u"Config")
        Config.resize(322, 232)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Config.sizePolicy().hasHeightForWidth())
        Config.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Config.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Config)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.pustButton_cancel = QPushButton(Config)
        self.pustButton_cancel.setObjectName(u"pustButton_cancel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pustButton_cancel.sizePolicy().hasHeightForWidth())
        self.pustButton_cancel.setSizePolicy(sizePolicy1)
        self.pustButton_cancel.setContextMenuPolicy(Qt.PreventContextMenu)

        self.gridLayout.addWidget(self.pustButton_cancel, 1, 1, 1, 1)

        self.pustButton_ok = QPushButton(Config)
        self.pustButton_ok.setObjectName(u"pustButton_ok")
        sizePolicy1.setHeightForWidth(self.pustButton_ok.sizePolicy().hasHeightForWidth())
        self.pustButton_ok.setSizePolicy(sizePolicy1)
        self.pustButton_ok.setContextMenuPolicy(Qt.PreventContextMenu)

        self.gridLayout.addWidget(self.pustButton_ok, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(Config)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_size = QWidget()
        self.tab_size.setObjectName(u"tab_size")
        self.gridLayout_2 = QGridLayout(self.tab_size)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_F = QLabel(self.tab_size)
        self.label_F.setObjectName(u"label_F")
        self.label_F.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_F, 0, 0, 1, 1)

        self.spinBox_resize_max_cnt = QSpinBox(self.tab_size)
        self.spinBox_resize_max_cnt.setObjectName(u"spinBox_resize_max_cnt")
        self.spinBox_resize_max_cnt.setMinimum(1)
        self.spinBox_resize_max_cnt.setMaximum(10)

        self.gridLayout_2.addWidget(self.spinBox_resize_max_cnt, 0, 1, 1, 1)

        self.label_F_8 = QLabel(self.tab_size)
        self.label_F_8.setObjectName(u"label_F_8")
        self.label_F_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_F_8, 0, 2, 1, 1)

        self.label_G = QLabel(self.tab_size)
        self.label_G.setObjectName(u"label_G")
        self.label_G.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_G, 1, 0, 1, 1)

        self.spinBox_resize_add_width_px = QSpinBox(self.tab_size)
        self.spinBox_resize_add_width_px.setObjectName(u"spinBox_resize_add_width_px")
        self.spinBox_resize_add_width_px.setMinimum(1)
        self.spinBox_resize_add_width_px.setMaximum(999)

        self.gridLayout_2.addWidget(self.spinBox_resize_add_width_px, 1, 1, 1, 1)

        self.label_F_9 = QLabel(self.tab_size)
        self.label_F_9.setObjectName(u"label_F_9")
        self.label_F_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_F_9, 1, 2, 1, 1)

        self.label_B = QLabel(self.tab_size)
        self.label_B.setObjectName(u"label_B")
        self.label_B.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_B, 2, 0, 1, 1)

        self.spinBox_base_width_toleft_px = QSpinBox(self.tab_size)
        self.spinBox_base_width_toleft_px.setObjectName(u"spinBox_base_width_toleft_px")
        self.spinBox_base_width_toleft_px.setMinimum(1)
        self.spinBox_base_width_toleft_px.setMaximum(9999)

        self.gridLayout_2.addWidget(self.spinBox_base_width_toleft_px, 2, 1, 1, 1)

        self.label_F_10 = QLabel(self.tab_size)
        self.label_F_10.setObjectName(u"label_F_10")
        self.label_F_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_F_10, 2, 2, 1, 1)

        self.label_A = QLabel(self.tab_size)
        self.label_A.setObjectName(u"label_A")
        self.label_A.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_A, 3, 0, 1, 1)

        self.spinBox_base_width_toright_px = QSpinBox(self.tab_size)
        self.spinBox_base_width_toright_px.setObjectName(u"spinBox_base_width_toright_px")
        self.spinBox_base_width_toright_px.setMinimum(1)
        self.spinBox_base_width_toright_px.setMaximum(9999)

        self.gridLayout_2.addWidget(self.spinBox_base_width_toright_px, 3, 1, 1, 1)

        self.label_F_11 = QLabel(self.tab_size)
        self.label_F_11.setObjectName(u"label_F_11")
        self.label_F_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_F_11, 3, 2, 1, 1)

        self.label_A_2 = QLabel(self.tab_size)
        self.label_A_2.setObjectName(u"label_A_2")
        self.label_A_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_A_2, 4, 0, 1, 1)

        self.spinBox_adjust_width_px = QSpinBox(self.tab_size)
        self.spinBox_adjust_width_px.setObjectName(u"spinBox_adjust_width_px")
        self.spinBox_adjust_width_px.setMinimum(1)
        self.spinBox_adjust_width_px.setMaximum(999)

        self.gridLayout_2.addWidget(self.spinBox_adjust_width_px, 4, 1, 1, 1)

        self.label_F_12 = QLabel(self.tab_size)
        self.label_F_12.setObjectName(u"label_F_12")
        self.label_F_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_F_12, 4, 2, 1, 1)

        self.checkBox_is_subtract_taskbar = QCheckBox(self.tab_size)
        self.checkBox_is_subtract_taskbar.setObjectName(u"checkBox_is_subtract_taskbar")
        self.checkBox_is_subtract_taskbar.setChecked(True)

        self.gridLayout_2.addWidget(self.checkBox_is_subtract_taskbar, 5, 0, 1, 3)

        self.tabWidget.addTab(self.tab_size, "")
        self.tab_position = QWidget()
        self.tab_position.setObjectName(u"tab_position")
        self.gridLayout_4 = QGridLayout(self.tab_position)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_B_2 = QLabel(self.tab_position)
        self.label_B_2.setObjectName(u"label_B_2")
        self.label_B_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_B_2, 0, 0, 1, 1)

        self.spinBox_adjust_x_px = QSpinBox(self.tab_position)
        self.spinBox_adjust_x_px.setObjectName(u"spinBox_adjust_x_px")
        self.spinBox_adjust_x_px.setMinimum(1)
        self.spinBox_adjust_x_px.setMaximum(999)

        self.gridLayout_4.addWidget(self.spinBox_adjust_x_px, 0, 1, 1, 1)

        self.label_F_7 = QLabel(self.tab_position)
        self.label_F_7.setObjectName(u"label_F_7")
        self.label_F_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_F_7, 0, 2, 1, 1)

        self.tabWidget.addTab(self.tab_position, "")
        self.tab_shortcutkey = QWidget()
        self.tab_shortcutkey.setObjectName(u"tab_shortcutkey")
        self.gridLayout_3 = QGridLayout(self.tab_shortcutkey)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.tab_shortcutkey)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.checkBox_windowleft_mod_ctrl = QCheckBox(self.groupBox)
        self.checkBox_windowleft_mod_ctrl.setObjectName(u"checkBox_windowleft_mod_ctrl")
        self.checkBox_windowleft_mod_ctrl.setChecked(True)

        self.gridLayout_5.addWidget(self.checkBox_windowleft_mod_ctrl, 0, 0, 1, 2)

        self.checkBox_windowleft_mod_shift = QCheckBox(self.groupBox)
        self.checkBox_windowleft_mod_shift.setObjectName(u"checkBox_windowleft_mod_shift")
        self.checkBox_windowleft_mod_shift.setChecked(True)

        self.gridLayout_5.addWidget(self.checkBox_windowleft_mod_shift, 1, 0, 1, 2)

        self.checkBox_windowleft_mod_alt = QCheckBox(self.groupBox)
        self.checkBox_windowleft_mod_alt.setObjectName(u"checkBox_windowleft_mod_alt")
        self.checkBox_windowleft_mod_alt.setChecked(True)

        self.gridLayout_5.addWidget(self.checkBox_windowleft_mod_alt, 2, 0, 1, 2)

        self.checkBox_windowleft_mod_win = QCheckBox(self.groupBox)
        self.checkBox_windowleft_mod_win.setObjectName(u"checkBox_windowleft_mod_win")
        self.checkBox_windowleft_mod_win.setChecked(True)

        self.gridLayout_5.addWidget(self.checkBox_windowleft_mod_win, 3, 0, 1, 2)

        self.label_A_3 = QLabel(self.groupBox)
        self.label_A_3.setObjectName(u"label_A_3")
        self.label_A_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_A_3, 4, 0, 1, 1)

        self.comboBox_Hotkey_WindowLeft = QComboBox(self.groupBox)
        self.comboBox_Hotkey_WindowLeft.setObjectName(u"comboBox_Hotkey_WindowLeft")

        self.gridLayout_5.addWidget(self.comboBox_Hotkey_WindowLeft, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab_shortcutkey)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.checkBox_windowright_mod_ctrl = QCheckBox(self.groupBox_2)
        self.checkBox_windowright_mod_ctrl.setObjectName(u"checkBox_windowright_mod_ctrl")
        self.checkBox_windowright_mod_ctrl.setChecked(True)

        self.gridLayout_6.addWidget(self.checkBox_windowright_mod_ctrl, 0, 0, 1, 2)

        self.checkBox_windowright_mod_shift = QCheckBox(self.groupBox_2)
        self.checkBox_windowright_mod_shift.setObjectName(u"checkBox_windowright_mod_shift")
        self.checkBox_windowright_mod_shift.setChecked(True)

        self.gridLayout_6.addWidget(self.checkBox_windowright_mod_shift, 1, 0, 1, 2)

        self.checkBox_windowright_mod_alt = QCheckBox(self.groupBox_2)
        self.checkBox_windowright_mod_alt.setObjectName(u"checkBox_windowright_mod_alt")
        self.checkBox_windowright_mod_alt.setChecked(True)

        self.gridLayout_6.addWidget(self.checkBox_windowright_mod_alt, 2, 0, 1, 1)

        self.checkBox_windowright_mod_win = QCheckBox(self.groupBox_2)
        self.checkBox_windowright_mod_win.setObjectName(u"checkBox_windowright_mod_win")
        self.checkBox_windowright_mod_win.setChecked(True)

        self.gridLayout_6.addWidget(self.checkBox_windowright_mod_win, 3, 0, 1, 1)

        self.label_A_5 = QLabel(self.groupBox_2)
        self.label_A_5.setObjectName(u"label_A_5")
        self.label_A_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_A_5, 4, 0, 1, 1)

        self.comboBox_Hotkey_WindowRight = QComboBox(self.groupBox_2)
        self.comboBox_Hotkey_WindowRight.setObjectName(u"comboBox_Hotkey_WindowRight")

        self.gridLayout_6.addWidget(self.comboBox_Hotkey_WindowRight, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_shortcutkey, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)


        self.retranslateUi(Config)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Config)
    # setupUi

    def retranslateUi(self, Config):
        Config.setWindowTitle(QCoreApplication.translate("Config", u"Fit Screen Window - \u8a2d\u5b9a", None))
        self.pustButton_cancel.setText(QCoreApplication.translate("Config", u"\u30ad\u30e3\u30f3\u30bb\u30eb", None))
        self.pustButton_ok.setText(QCoreApplication.translate("Config", u"OK", None))
        self.label_F.setText(QCoreApplication.translate("Config", u"\u30ea\u30b5\u30a4\u30ba\u6700\u5927\u56de\u6570(1\uff5e10)", None))
        self.label_F_8.setText(QCoreApplication.translate("Config", u"\u56de", None))
        self.label_G.setText(QCoreApplication.translate("Config", u"\u30ea\u30b5\u30a4\u30ba\u6bce\u52a0\u7b97\u30b5\u30a4\u30ba(1\uff5e999)", None))
        self.label_F_9.setText(QCoreApplication.translate("Config", u"px", None))
        self.label_B.setText(QCoreApplication.translate("Config", u"\u57fa\u6e96\u30b5\u30a4\u30ba - \u5de6\u914d\u7f6e(1\uff5e9999)", None))
        self.label_F_10.setText(QCoreApplication.translate("Config", u"px", None))
        self.label_A.setText(QCoreApplication.translate("Config", u"\u57fa\u6e96\u30b5\u30a4\u30ba - \u53f3\u914d\u7f6e(1\uff5e9999)", None))
        self.label_F_11.setText(QCoreApplication.translate("Config", u"px", None))
        self.label_A_2.setText(QCoreApplication.translate("Config", u"\u8abf\u6574\u7528\u52a0\u7b97\u30b5\u30a4\u30ba(1\uff5e999)", None))
        self.label_F_12.setText(QCoreApplication.translate("Config", u"px", None))
        self.checkBox_is_subtract_taskbar.setText(QCoreApplication.translate("Config", u"\u30bf\u30b9\u30af\u30d0\u30fc\u306e\u9ad8\u3055\u3092\u6e1b\u7b97\u3057\u3066\u30ea\u30b5\u30a4\u30ba(\u4e0b\u4f4d\u7f6e\u306e\u307f)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_size), QCoreApplication.translate("Config", u"\u30b5\u30a4\u30ba", None))
        self.label_B_2.setText(QCoreApplication.translate("Config", u"\u8abf\u6574\u7528\u79fb\u52d5\u4f4d\u7f6e - x(1\uff5e999)", None))
        self.label_F_7.setText(QCoreApplication.translate("Config", u"px", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_position), QCoreApplication.translate("Config", u"\u4f4d\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Config", u"\u30a6\u30a3\u30f3\u30c9\u30a6\u5de6\u914d\u7f6e", None))
        self.checkBox_windowleft_mod_ctrl.setText(QCoreApplication.translate("Config", u"Ctrl", None))
        self.checkBox_windowleft_mod_shift.setText(QCoreApplication.translate("Config", u"Shift", None))
        self.checkBox_windowleft_mod_alt.setText(QCoreApplication.translate("Config", u"Alt", None))
        self.checkBox_windowleft_mod_win.setText(QCoreApplication.translate("Config", u"Win", None))
        self.label_A_3.setText(QCoreApplication.translate("Config", u"\u901a\u5e38\u30ad\u30fc", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Config", u"\u30a6\u30a3\u30f3\u30c9\u30a6\u53f3\u914d\u7f6e", None))
        self.checkBox_windowright_mod_ctrl.setText(QCoreApplication.translate("Config", u"Ctrl", None))
        self.checkBox_windowright_mod_shift.setText(QCoreApplication.translate("Config", u"Shift", None))
        self.checkBox_windowright_mod_alt.setText(QCoreApplication.translate("Config", u"Alt", None))
        self.checkBox_windowright_mod_win.setText(QCoreApplication.translate("Config", u"Win", None))
        self.label_A_5.setText(QCoreApplication.translate("Config", u"\u901a\u5e38\u30ad\u30fc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_shortcutkey), QCoreApplication.translate("Config", u"\u30b7\u30e7\u30fc\u30c8\u30ab\u30c3\u30c8\u30ad\u30fc", None))
    # retranslateUi
