# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configgui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
from src.gui import resource_rc

class Ui_ConfigGUI(object):
    def setupUi(self, ConfigGUI):
        if not ConfigGUI.objectName():
            ConfigGUI.setObjectName(u"ConfigGUI")
        ConfigGUI.resize(930, 560)
        ConfigGUI.setMinimumSize(QSize(930, 560))
        #ConfigGUI.setAnimated(True)
        self.entireStyleSheet = QWidget(ConfigGUI)
        self.entireStyleSheet.setObjectName(u"entireStyleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.entireStyleSheet.setFont(font)
        self.entireStyleSheet.setStyleSheet(u"/* ========================================================================= */\n"
"/* ========================================================================= */\n"
"/* \u5168\u4f53\u5171\u6709\u8a2d\u5b9a */\n"
"/* ========================================================================= */\n"
"/* ========================================================================= */\n"
"\n"
"/* ------------------------------------------------------------------------- */\n"
"/* \u30a6\u30a3\u30b8\u30a7\u30c3\u30c8\u5168\u4f53 */\n"
"/* ------------------------------------------------------------------------- */\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"#entireBg {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------- */\n"
"/* LineEdit */\n"
"/* ------------------------------------------------------------------------- */\n"
"QLineEdit {\n"
"	background-color:"
                        " rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #FF5F5F;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------- */\n"
"/* CheckBox */\n"
"/* ------------------------------------------------------------------------- */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"    background-image: url(:/images/icon-check.png);\n"
"}\n"
"\n"
"/* ------------------------------------------"
                        "------------------------------- */\n"
"/* ComboBox */\n"
"/* ------------------------------------------------------------------------- */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"    background-image: url(:/images/icon-arrowbottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: #FF5F5F;	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"\n"
"/* =========================="
                        "=============================================== */\n"
"/* ========================================================================= */\n"
"/* \u30a6\u30a3\u30b8\u30a7\u30c3\u30c8\u9818\u57df\u6bce\u500b\u5225\u8a2d\u5b9a */\n"
"/* ========================================================================= */\n"
"/* ========================================================================= */\n"
"\n"
"/* ------------------------------------------------------------------------- */\n"
"/* LeftMenu */\n"
"/* ------------------------------------------------------------------------- */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#leftTopLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#leftTitleApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"\n"
"#leftMenuFrame .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-le"
                        "ft: 44px;\n"
"}\n"
"#leftMenuFrame .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#leftMenuFrame .QPushButton:pressed {	\n"
"	background-color: #FF5F5F;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* ------------------------------------------------------------------------- */\n"
"/* RightBox */\n"
"/* ------------------------------------------------------------------------- */\n"
"#rightTopBg{\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"#rightButtonsFrame .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtonsFrame .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtonsFrame .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Pages Container */\n"
"#rightBoxPagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
""
                        "#rightBoxPagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#rightBoxPagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* Bottom Bar */\n"
"#rightBoxBottomBar { background-color: rgb(44, 49, 58); }\n"
"#rightBoxBottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }")
        self.entireBg = QFrame(self.entireStyleSheet)
        self.entireBg.setObjectName(u"entireBg")
        self.entireBg.setGeometry(QRect(0, 0, 920, 549))
        self.entireBg.setStyleSheet(u"")
        self.entireBg.setFrameShape(QFrame.NoFrame)
        self.entireBg.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.entireBg)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.entireBg)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(190, 0))
        self.leftMenuBg.setMaximumSize(QSize(190, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftTopLogo = QFrame(self.leftMenuBg)
        self.leftTopLogo.setObjectName(u"leftTopLogo")
        self.leftTopLogo.setMinimumSize(QSize(0, 50))
        self.leftTopLogo.setMaximumSize(QSize(16777215, 50))
        self.leftTopLogo.setFrameShape(QFrame.NoFrame)
        self.leftTopLogo.setFrameShadow(QFrame.Raised)
        self.leftTitleApp = QLabel(self.leftTopLogo)
        self.leftTitleApp.setObjectName(u"leftTitleApp")
        self.leftTitleApp.setGeometry(QRect(20, 10, 151, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setBold(False)
        font1.setItalic(False)
        self.leftTitleApp.setFont(font1)
        self.leftTitleApp.setStyleSheet(u"font-size: 17px;")
        self.leftTitleApp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.leftTopLogo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuMainContent = QFrame(self.leftMenuFrame)
        self.leftMenuMainContent.setObjectName(u"leftMenuMainContent")
        self.leftMenuMainContent.setFrameShape(QFrame.NoFrame)
        self.leftMenuMainContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.leftMenuMainContent)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_size = QPushButton(self.leftMenuMainContent)
        self.pushButton_size.setObjectName(u"pushButton_size")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_size.sizePolicy().hasHeightForWidth())
        self.pushButton_size.setSizePolicy(sizePolicy)
        self.pushButton_size.setMinimumSize(QSize(0, 45))
        self.pushButton_size.setFont(font)
        self.pushButton_size.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_size.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_size.setStyleSheet(u"background-image: url(:/images/icon-size.png);")

        self.verticalLayout_8.addWidget(self.pushButton_size)

        self.pushButton_position = QPushButton(self.leftMenuMainContent)
        self.pushButton_position.setObjectName(u"pushButton_position")
        sizePolicy.setHeightForWidth(self.pushButton_position.sizePolicy().hasHeightForWidth())
        self.pushButton_position.setSizePolicy(sizePolicy)
        self.pushButton_position.setMinimumSize(QSize(0, 45))
        self.pushButton_position.setFont(font)
        self.pushButton_position.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_position.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_position.setStyleSheet(u"background-image: url(:/images/icon-position.png);")

        self.verticalLayout_8.addWidget(self.pushButton_position)

        self.pushButton_hotkey = QPushButton(self.leftMenuMainContent)
        self.pushButton_hotkey.setObjectName(u"pushButton_hotkey")
        sizePolicy.setHeightForWidth(self.pushButton_hotkey.sizePolicy().hasHeightForWidth())
        self.pushButton_hotkey.setSizePolicy(sizePolicy)
        self.pushButton_hotkey.setMinimumSize(QSize(0, 45))
        self.pushButton_hotkey.setFont(font)
        self.pushButton_hotkey.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_hotkey.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_hotkey.setStyleSheet(u"background-image: url(:/images/icon-hotkey.png);")

        self.verticalLayout_8.addWidget(self.pushButton_hotkey)

        self.pushButton_saveandexit = QPushButton(self.leftMenuMainContent)
        self.pushButton_saveandexit.setObjectName(u"pushButton_saveandexit")
        sizePolicy.setHeightForWidth(self.pushButton_saveandexit.sizePolicy().hasHeightForWidth())
        self.pushButton_saveandexit.setSizePolicy(sizePolicy)
        self.pushButton_saveandexit.setMinimumSize(QSize(0, 45))
        self.pushButton_saveandexit.setFont(font)
        self.pushButton_saveandexit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_saveandexit.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_saveandexit.setStyleSheet(u"background-image: url(:/images/icon-save.png);")

        self.verticalLayout_8.addWidget(self.pushButton_saveandexit)

        self.pushButton_cancel = QPushButton(self.leftMenuMainContent)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)
        self.pushButton_cancel.setMinimumSize(QSize(0, 45))
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_cancel.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_cancel.setStyleSheet(u"background-image: url(:/images/icon-cancel.png);")

        self.verticalLayout_8.addWidget(self.pushButton_cancel)

        self.verticalSpacer = QSpacerItem(20, 300, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.pushButton_initialize_setting = QPushButton(self.leftMenuMainContent)
        self.pushButton_initialize_setting.setObjectName(u"pushButton_initialize_setting")
        sizePolicy.setHeightForWidth(self.pushButton_initialize_setting.sizePolicy().hasHeightForWidth())
        self.pushButton_initialize_setting.setSizePolicy(sizePolicy)
        self.pushButton_initialize_setting.setMinimumSize(QSize(0, 45))
        self.pushButton_initialize_setting.setFont(font)
        self.pushButton_initialize_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_initialize_setting.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_initialize_setting.setStyleSheet(u"background-image: url(:/images/icon-initializesetting.png);")

        self.verticalLayout_8.addWidget(self.pushButton_initialize_setting)


        self.verticalMenuLayout.addWidget(self.leftMenuMainContent, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)

        self.leftMenuFrame.raise_()
        self.leftTopLogo.raise_()

        self.appLayout.addWidget(self.leftMenuBg)

        self.rightBoxBg = QFrame(self.entireBg)
        self.rightBoxBg.setObjectName(u"rightBoxBg")
        self.rightBoxBg.setFrameShape(QFrame.NoFrame)
        self.rightBoxBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.rightBoxBg)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rightTopBg = QFrame(self.rightBoxBg)
        self.rightTopBg.setObjectName(u"rightTopBg")
        self.rightTopBg.setMinimumSize(QSize(0, 50))
        self.rightTopBg.setMaximumSize(QSize(16777215, 50))
        self.rightTopBg.setFrameShape(QFrame.NoFrame)
        self.rightTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.rightTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.rightButtonsFrame = QFrame(self.rightTopBg)
        self.rightButtonsFrame.setObjectName(u"rightButtonsFrame")
        self.rightButtonsFrame.setMinimumSize(QSize(0, 28))
        self.rightButtonsFrame.setFrameShape(QFrame.NoFrame)
        self.rightButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtonsFrame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_close = QPushButton(self.rightButtonsFrame)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(28, 28))
        self.pushButton_close.setMaximumSize(QSize(28, 28))
        self.pushButton_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet(u"background-image: url(:/images/icon-cancel.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon)
        self.pushButton_close.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.pushButton_close)


        self.horizontalLayout.addWidget(self.rightButtonsFrame, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.rightTopBg)

        self.rightBoxFrame = QFrame(self.rightBoxBg)
        self.rightBoxFrame.setObjectName(u"rightBoxFrame")
        self.rightBoxFrame.setFrameShape(QFrame.NoFrame)
        self.rightBoxFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.rightBoxFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.rightBoxMainContent = QFrame(self.rightBoxFrame)
        self.rightBoxMainContent.setObjectName(u"rightBoxMainContent")
        self.rightBoxMainContent.setFrameShape(QFrame.NoFrame)
        self.rightBoxMainContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.rightBoxMainContent)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.rightBoxPagesContainer = QFrame(self.rightBoxMainContent)
        self.rightBoxPagesContainer.setObjectName(u"rightBoxPagesContainer")
        self.rightBoxPagesContainer.setStyleSheet(u"")
        self.rightBoxPagesContainer.setFrameShape(QFrame.NoFrame)
        self.rightBoxPagesContainer.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.rightBoxPagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 9, 700, 1198))
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_size = QWidget()
        self.page_size.setObjectName(u"page_size")
        self.page_size.setStyleSheet(u"b")
        self.frame = QFrame(self.page_size)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 250, 200))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(250, 200))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(12)
        self.gridLayout_5.setContentsMargins(-1, -1, 9, -1)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.labelBoxBlenderInstalation = QLabel(self.groupBox)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setGeometry(QRect(10, 27, 57, 18))
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")
        self.lineEdit_base_width_toleft_px = QLineEdit(self.groupBox)
        self.lineEdit_base_width_toleft_px.setObjectName(u"lineEdit_base_width_toleft_px")
        self.lineEdit_base_width_toleft_px.setGeometry(QRect(10, 60, 120, 30))
        self.lineEdit_base_width_toleft_px.setMinimumSize(QSize(0, 30))
        self.lineEdit_base_width_toleft_px.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.labelBoxBlenderInstalation_2 = QLabel(self.groupBox)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setGeometry(QRect(140, 70, 16, 18))
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")
        self.checkBox_is_reverse_direction_windowleft = QCheckBox(self.groupBox)
        self.checkBox_is_reverse_direction_windowleft.setObjectName(u"checkBox_is_reverse_direction_windowleft")
        self.checkBox_is_reverse_direction_windowleft.setGeometry(QRect(10, 110, 211, 21))
        self.checkBox_is_reverse_direction_windowleft.setAutoFillBackground(False)
        self.checkBox_is_reverse_direction_windowleft.setStyleSheet(u"")
        self.labelVersion_4 = QLabel(self.groupBox)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setGeometry(QRect(82, 27, 141, 18))
        self.labelVersion_4.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.page_size)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(270, 10, 250, 200))
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(250, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.groupBox_3 = QGroupBox(self.frame_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 10, 230, 180))
        self.labelBoxBlenderInstalation_5 = QLabel(self.groupBox_3)
        self.labelBoxBlenderInstalation_5.setObjectName(u"labelBoxBlenderInstalation_5")
        self.labelBoxBlenderInstalation_5.setGeometry(QRect(10, 27, 57, 18))
        self.labelBoxBlenderInstalation_5.setFont(font)
        self.labelBoxBlenderInstalation_5.setStyleSheet(u"")
        self.lineEdit_base_width_toright_px = QLineEdit(self.groupBox_3)
        self.lineEdit_base_width_toright_px.setObjectName(u"lineEdit_base_width_toright_px")
        self.lineEdit_base_width_toright_px.setGeometry(QRect(10, 60, 120, 30))
        self.lineEdit_base_width_toright_px.setMinimumSize(QSize(0, 30))
        self.lineEdit_base_width_toright_px.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.labelBoxBlenderInstalation_6 = QLabel(self.groupBox_3)
        self.labelBoxBlenderInstalation_6.setObjectName(u"labelBoxBlenderInstalation_6")
        self.labelBoxBlenderInstalation_6.setGeometry(QRect(140, 70, 16, 18))
        self.labelBoxBlenderInstalation_6.setFont(font)
        self.labelBoxBlenderInstalation_6.setStyleSheet(u"")
        self.checkBox_is_reverse_direction_windowright = QCheckBox(self.groupBox_3)
        self.checkBox_is_reverse_direction_windowright.setObjectName(u"checkBox_is_reverse_direction_windowright")
        self.checkBox_is_reverse_direction_windowright.setGeometry(QRect(10, 110, 211, 21))
        self.checkBox_is_reverse_direction_windowright.setAutoFillBackground(False)
        self.checkBox_is_reverse_direction_windowright.setStyleSheet(u"")
        self.labelVersion_6 = QLabel(self.groupBox_3)
        self.labelVersion_6.setObjectName(u"labelVersion_6")
        self.labelVersion_6.setGeometry(QRect(82, 27, 141, 18))
        self.labelVersion_6.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_6.setLineWidth(1)
        self.labelVersion_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.frame_3 = QFrame(self.page_size)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 210, 511, 241))
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(250, 200))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.groupBox_4 = QGroupBox(self.frame_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 10, 491, 221))
        self.labelBoxBlenderInstalation_7 = QLabel(self.groupBox_4)
        self.labelBoxBlenderInstalation_7.setObjectName(u"labelBoxBlenderInstalation_7")
        self.labelBoxBlenderInstalation_7.setGeometry(QRect(10, 27, 131, 18))
        self.labelBoxBlenderInstalation_7.setFont(font)
        self.labelBoxBlenderInstalation_7.setStyleSheet(u"")
        self.lineEdit_resize_max_cnt = QLineEdit(self.groupBox_4)
        self.lineEdit_resize_max_cnt.setObjectName(u"lineEdit_resize_max_cnt")
        self.lineEdit_resize_max_cnt.setGeometry(QRect(230, 20, 120, 30))
        self.lineEdit_resize_max_cnt.setMinimumSize(QSize(0, 30))
        self.lineEdit_resize_max_cnt.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.labelBoxBlenderInstalation_8 = QLabel(self.groupBox_4)
        self.labelBoxBlenderInstalation_8.setObjectName(u"labelBoxBlenderInstalation_8")
        self.labelBoxBlenderInstalation_8.setGeometry(QRect(360, 30, 16, 18))
        self.labelBoxBlenderInstalation_8.setFont(font)
        self.labelBoxBlenderInstalation_8.setStyleSheet(u"")
        self.checkBox_is_subtract_taskbar = QCheckBox(self.groupBox_4)
        self.checkBox_is_subtract_taskbar.setObjectName(u"checkBox_is_subtract_taskbar")
        self.checkBox_is_subtract_taskbar.setGeometry(QRect(10, 150, 321, 21))
        self.checkBox_is_subtract_taskbar.setAutoFillBackground(False)
        self.checkBox_is_subtract_taskbar.setStyleSheet(u"")
        self.labelVersion_7 = QLabel(self.groupBox_4)
        self.labelVersion_7.setObjectName(u"labelVersion_7")
        self.labelVersion_7.setGeometry(QRect(150, 30, 81, 18))
        self.labelVersion_7.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_7.setLineWidth(1)
        self.labelVersion_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelBoxBlenderInstalation_9 = QLabel(self.groupBox_4)
        self.labelBoxBlenderInstalation_9.setObjectName(u"labelBoxBlenderInstalation_9")
        self.labelBoxBlenderInstalation_9.setGeometry(QRect(360, 70, 16, 18))
        self.labelBoxBlenderInstalation_9.setFont(font)
        self.labelBoxBlenderInstalation_9.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_10 = QLabel(self.groupBox_4)
        self.labelBoxBlenderInstalation_10.setObjectName(u"labelBoxBlenderInstalation_10")
        self.labelBoxBlenderInstalation_10.setGeometry(QRect(10, 67, 131, 18))
        self.labelBoxBlenderInstalation_10.setFont(font)
        self.labelBoxBlenderInstalation_10.setStyleSheet(u"")
        self.lineEdit_resize_add_width_px = QLineEdit(self.groupBox_4)
        self.lineEdit_resize_add_width_px.setObjectName(u"lineEdit_resize_add_width_px")
        self.lineEdit_resize_add_width_px.setGeometry(QRect(230, 60, 120, 30))
        self.lineEdit_resize_add_width_px.setMinimumSize(QSize(0, 30))
        self.lineEdit_resize_add_width_px.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.labelVersion_8 = QLabel(self.groupBox_4)
        self.labelVersion_8.setObjectName(u"labelVersion_8")
        self.labelVersion_8.setGeometry(QRect(150, 70, 81, 18))
        self.labelVersion_8.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_8.setLineWidth(1)
        self.labelVersion_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelBoxBlenderInstalation_11 = QLabel(self.groupBox_4)
        self.labelBoxBlenderInstalation_11.setObjectName(u"labelBoxBlenderInstalation_11")
        self.labelBoxBlenderInstalation_11.setGeometry(QRect(360, 110, 16, 18))
        self.labelBoxBlenderInstalation_11.setFont(font)
        self.labelBoxBlenderInstalation_11.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_12 = QLabel(self.groupBox_4)
        self.labelBoxBlenderInstalation_12.setObjectName(u"labelBoxBlenderInstalation_12")
        self.labelBoxBlenderInstalation_12.setGeometry(QRect(10, 107, 131, 18))
        self.labelBoxBlenderInstalation_12.setFont(font)
        self.labelBoxBlenderInstalation_12.setStyleSheet(u"")
        self.labelVersion_9 = QLabel(self.groupBox_4)
        self.labelVersion_9.setObjectName(u"labelVersion_9")
        self.labelVersion_9.setGeometry(QRect(150, 110, 81, 18))
        self.labelVersion_9.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_9.setLineWidth(1)
        self.labelVersion_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_adjust_width_px = QLineEdit(self.groupBox_4)
        self.lineEdit_adjust_width_px.setObjectName(u"lineEdit_adjust_width_px")
        self.lineEdit_adjust_width_px.setGeometry(QRect(230, 100, 120, 30))
        self.lineEdit_adjust_width_px.setMinimumSize(QSize(0, 30))
        self.lineEdit_adjust_width_px.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.stackedWidget.addWidget(self.page_size)
        self.page_position = QWidget()
        self.page_position.setObjectName(u"page_position")
        self.frame_4 = QFrame(self.page_position)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 451, 111))
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setMinimumSize(QSize(250, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.groupBox_2 = QGroupBox(self.frame_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 441, 81))
        self.labelBoxBlenderInstalation_3 = QLabel(self.groupBox_2)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setGeometry(QRect(10, 27, 111, 18))
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")
        self.lineEdit_adjust_x_px = QLineEdit(self.groupBox_2)
        self.lineEdit_adjust_x_px.setObjectName(u"lineEdit_adjust_x_px")
        self.lineEdit_adjust_x_px.setGeometry(QRect(210, 20, 120, 30))
        self.lineEdit_adjust_x_px.setMinimumSize(QSize(0, 30))
        self.lineEdit_adjust_x_px.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lineEdit_adjust_x_px.setMaxLength(5)
        self.labelBoxBlenderInstalation_4 = QLabel(self.groupBox_2)
        self.labelBoxBlenderInstalation_4.setObjectName(u"labelBoxBlenderInstalation_4")
        self.labelBoxBlenderInstalation_4.setGeometry(QRect(340, 30, 16, 18))
        self.labelBoxBlenderInstalation_4.setFont(font)
        self.labelBoxBlenderInstalation_4.setStyleSheet(u"")
        self.labelVersion_5 = QLabel(self.groupBox_2)
        self.labelVersion_5.setObjectName(u"labelVersion_5")
        self.labelVersion_5.setGeometry(QRect(120, 30, 86, 18))
        self.labelVersion_5.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_5.setLineWidth(1)
        self.labelVersion_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_position)
        self.page_hotkey = QWidget()
        self.page_hotkey.setObjectName(u"page_hotkey")
        self.frame_5 = QFrame(self.page_hotkey)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 10, 250, 241))
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMinimumSize(QSize(250, 200))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.groupBox_5 = QGroupBox(self.frame_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 10, 230, 221))
        self.checkBox_windowleft_mod_ctrl = QCheckBox(self.groupBox_5)
        self.checkBox_windowleft_mod_ctrl.setObjectName(u"checkBox_windowleft_mod_ctrl")
        self.checkBox_windowleft_mod_ctrl.setGeometry(QRect(10, 40, 115, 21))
        self.checkBox_windowleft_mod_ctrl.setAutoFillBackground(False)
        self.checkBox_windowleft_mod_ctrl.setStyleSheet(u"")
        self.checkBox_windowleft_mod_shift = QCheckBox(self.groupBox_5)
        self.checkBox_windowleft_mod_shift.setObjectName(u"checkBox_windowleft_mod_shift")
        self.checkBox_windowleft_mod_shift.setGeometry(QRect(10, 70, 115, 21))
        self.checkBox_windowleft_mod_shift.setAutoFillBackground(False)
        self.checkBox_windowleft_mod_shift.setStyleSheet(u"")
        self.checkBox_windowleft_mod_alt = QCheckBox(self.groupBox_5)
        self.checkBox_windowleft_mod_alt.setObjectName(u"checkBox_windowleft_mod_alt")
        self.checkBox_windowleft_mod_alt.setGeometry(QRect(10, 100, 115, 21))
        self.checkBox_windowleft_mod_alt.setAutoFillBackground(False)
        self.checkBox_windowleft_mod_alt.setStyleSheet(u"")
        self.checkBox_windowleft_mod_win = QCheckBox(self.groupBox_5)
        self.checkBox_windowleft_mod_win.setObjectName(u"checkBox_windowleft_mod_win")
        self.checkBox_windowleft_mod_win.setGeometry(QRect(10, 130, 115, 21))
        self.checkBox_windowleft_mod_win.setAutoFillBackground(False)
        self.checkBox_windowleft_mod_win.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_13 = QLabel(self.groupBox_5)
        self.labelBoxBlenderInstalation_13.setObjectName(u"labelBoxBlenderInstalation_13")
        self.labelBoxBlenderInstalation_13.setGeometry(QRect(10, 170, 101, 18))
        self.labelBoxBlenderInstalation_13.setFont(font)
        self.labelBoxBlenderInstalation_13.setStyleSheet(u"")
        self.comboBox_Hotkey_WindowLeft = QComboBox(self.groupBox_5)
        self.comboBox_Hotkey_WindowLeft.addItem("")
        self.comboBox_Hotkey_WindowLeft.addItem("")
        self.comboBox_Hotkey_WindowLeft.addItem("")
        self.comboBox_Hotkey_WindowLeft.setObjectName(u"comboBox_Hotkey_WindowLeft")
        self.comboBox_Hotkey_WindowLeft.setGeometry(QRect(80, 170, 131, 34))
        self.comboBox_Hotkey_WindowLeft.setFont(font)
        self.comboBox_Hotkey_WindowLeft.setAutoFillBackground(False)
        self.comboBox_Hotkey_WindowLeft.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_Hotkey_WindowLeft.setIconSize(QSize(16, 16))
        self.comboBox_Hotkey_WindowLeft.setFrame(True)
        self.frame_6 = QFrame(self.page_hotkey)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(290, 10, 250, 241))
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(250, 200))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.groupBox_6 = QGroupBox(self.frame_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 10, 230, 221))
        self.checkBox_windowright_mod_ctrl = QCheckBox(self.groupBox_6)
        self.checkBox_windowright_mod_ctrl.setObjectName(u"checkBox_windowright_mod_ctrl")
        self.checkBox_windowright_mod_ctrl.setGeometry(QRect(10, 40, 115, 21))
        self.checkBox_windowright_mod_ctrl.setAutoFillBackground(False)
        self.checkBox_windowright_mod_ctrl.setStyleSheet(u"")
        self.checkBox_windowright_mod_shift = QCheckBox(self.groupBox_6)
        self.checkBox_windowright_mod_shift.setObjectName(u"checkBox_windowright_mod_shift")
        self.checkBox_windowright_mod_shift.setGeometry(QRect(10, 70, 115, 21))
        self.checkBox_windowright_mod_shift.setAutoFillBackground(False)
        self.checkBox_windowright_mod_shift.setStyleSheet(u"")
        self.checkBox_windowright_mod_alt = QCheckBox(self.groupBox_6)
        self.checkBox_windowright_mod_alt.setObjectName(u"checkBox_windowright_mod_alt")
        self.checkBox_windowright_mod_alt.setGeometry(QRect(10, 100, 115, 21))
        self.checkBox_windowright_mod_alt.setAutoFillBackground(False)
        self.checkBox_windowright_mod_alt.setStyleSheet(u"")
        self.checkBox_windowright_mod_win = QCheckBox(self.groupBox_6)
        self.checkBox_windowright_mod_win.setObjectName(u"checkBox_windowright_mod_win")
        self.checkBox_windowright_mod_win.setGeometry(QRect(10, 130, 115, 21))
        self.checkBox_windowright_mod_win.setAutoFillBackground(False)
        self.checkBox_windowright_mod_win.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_14 = QLabel(self.groupBox_6)
        self.labelBoxBlenderInstalation_14.setObjectName(u"labelBoxBlenderInstalation_14")
        self.labelBoxBlenderInstalation_14.setGeometry(QRect(10, 170, 101, 18))
        self.labelBoxBlenderInstalation_14.setFont(font)
        self.labelBoxBlenderInstalation_14.setStyleSheet(u"")
        self.comboBox_Hotkey_WindowRight = QComboBox(self.groupBox_6)
        self.comboBox_Hotkey_WindowRight.addItem("")
        self.comboBox_Hotkey_WindowRight.addItem("")
        self.comboBox_Hotkey_WindowRight.addItem("")
        self.comboBox_Hotkey_WindowRight.setObjectName(u"comboBox_Hotkey_WindowRight")
        self.comboBox_Hotkey_WindowRight.setGeometry(QRect(80, 170, 131, 34))
        self.comboBox_Hotkey_WindowRight.setFont(font)
        self.comboBox_Hotkey_WindowRight.setAutoFillBackground(False)
        self.comboBox_Hotkey_WindowRight.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_Hotkey_WindowRight.setIconSize(QSize(16, 16))
        self.comboBox_Hotkey_WindowRight.setFrame(True)
        self.stackedWidget.addWidget(self.page_hotkey)

        self.horizontalLayout_4.addWidget(self.rightBoxPagesContainer)


        self.verticalLayout_6.addWidget(self.rightBoxMainContent)

        self.rightBoxBottomBar = QFrame(self.rightBoxFrame)
        self.rightBoxBottomBar.setObjectName(u"rightBoxBottomBar")
        self.rightBoxBottomBar.setMinimumSize(QSize(0, 22))
        self.rightBoxBottomBar.setMaximumSize(QSize(16777215, 22))
        self.rightBoxBottomBar.setFrameShape(QFrame.NoFrame)
        self.rightBoxBottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.rightBoxBottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_settingmenu = QLabel(self.rightBoxBottomBar)
        self.label_settingmenu.setObjectName(u"label_settingmenu")
        self.label_settingmenu.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(False)
        font2.setItalic(False)
        self.label_settingmenu.setFont(font2)
        self.label_settingmenu.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_settingmenu)

        self.label_version = QLabel(self.rightBoxBottomBar)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_version)

        self.frame_size_grip = QFrame(self.rightBoxBottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.rightBoxBottomBar)


        self.verticalLayout_2.addWidget(self.rightBoxFrame)


        self.appLayout.addWidget(self.rightBoxBg)

        #ConfigGUI.setCentralWidget(self.entireStyleSheet)

        self.retranslateUi(ConfigGUI)
        self.pushButton_size.pressed.connect(self.stackedWidget.update)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(ConfigGUI)
    # setupUi

    def retranslateUi(self, ConfigGUI):
        ConfigGUI.setWindowTitle(QCoreApplication.translate("ConfigGUI", u"MainWindow", None))
        self.leftTitleApp.setText(QCoreApplication.translate("ConfigGUI", u"Fit Screen Window", None))
        self.pushButton_size.setText(QCoreApplication.translate("ConfigGUI", u"\u30b5\u30a4\u30ba", None))
        self.pushButton_position.setText(QCoreApplication.translate("ConfigGUI", u"\u4f4d\u7f6e", None))
        self.pushButton_hotkey.setText(QCoreApplication.translate("ConfigGUI", u"\u30b7\u30e7\u30fc\u30c8\u30ab\u30c3\u30c8\u30ad\u30fc", None))
        self.pushButton_saveandexit.setText(QCoreApplication.translate("ConfigGUI", u"\u4fdd\u5b58\u3057\u3066\u7d42\u4e86", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("ConfigGUI", u"\u30ad\u30e3\u30f3\u30bb\u30eb", None))
        self.pushButton_initialize_setting.setText(QCoreApplication.translate("ConfigGUI", u"\u521d\u671f\u8a2d\u5b9a", None))
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_close.setText("")
#if QT_CONFIG(whatsthis)
        self.rightBoxPagesContainer.setWhatsThis(QCoreApplication.translate("ConfigGUI", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBox.setTitle(QCoreApplication.translate("ConfigGUI", u"\u30a6\u30a3\u30f3\u30c9\u30a6\u5de6\u914d\u7f6e", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("ConfigGUI", u"\u57fa\u6e96\u30b5\u30a4\u30ba", None))
        self.lineEdit_base_width_toleft_px.setText("")
        self.lineEdit_base_width_toleft_px.setPlaceholderText(QCoreApplication.translate("ConfigGUI", u"\u6570\u5024\u3092\u5165\u529b", None))
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("ConfigGUI", u"px", None))
        self.checkBox_is_reverse_direction_windowleft.setText(QCoreApplication.translate("ConfigGUI", u"\u9006\u65b9\u5411\u306b\u30ea\u30b5\u30a4\u30ba", None))
        self.labelVersion_4.setText(QCoreApplication.translate("ConfigGUI", u"(\u7bc4\u56f2 1\uff5e9999)", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ConfigGUI", u"\u30a6\u30a3\u30f3\u30c9\u30a6\u53f3\u914d\u7f6e", None))
        self.labelBoxBlenderInstalation_5.setText(QCoreApplication.translate("ConfigGUI", u"\u57fa\u6e96\u30b5\u30a4\u30ba", None))
        self.lineEdit_base_width_toright_px.setText("")
        self.lineEdit_base_width_toright_px.setPlaceholderText(QCoreApplication.translate("ConfigGUI", u"\u6570\u5024\u3092\u5165\u529b", None))
        self.labelBoxBlenderInstalation_6.setText(QCoreApplication.translate("ConfigGUI", u"px", None))
        self.checkBox_is_reverse_direction_windowright.setText(QCoreApplication.translate("ConfigGUI", u"\u9006\u65b9\u5411\u306b\u30ea\u30b5\u30a4\u30ba", None))
        self.labelVersion_6.setText(QCoreApplication.translate("ConfigGUI", u"(\u7bc4\u56f2 1\uff5e9999)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ConfigGUI", u"\u5171\u901a\u8a2d\u5b9a", None))
        self.labelBoxBlenderInstalation_7.setText(QCoreApplication.translate("ConfigGUI", u"\u30ea\u30b5\u30a4\u30ba\u6700\u5927\u56de\u6570", None))
        self.lineEdit_resize_max_cnt.setText("")
        self.lineEdit_resize_max_cnt.setPlaceholderText(QCoreApplication.translate("ConfigGUI", u"\u6570\u5024\u3092\u5165\u529b", None))
        self.labelBoxBlenderInstalation_8.setText(QCoreApplication.translate("ConfigGUI", u"\u56de", None))
        self.checkBox_is_subtract_taskbar.setText(QCoreApplication.translate("ConfigGUI", u"\u30bf\u30b9\u30af\u30d0\u30fc\u306e\u30b5\u30a4\u30ba\u3092\u6e1b\u7b97\u3057\u3066\u30ea\u30b5\u30a4\u30ba", None))
        self.labelVersion_7.setText(QCoreApplication.translate("ConfigGUI", u"(\u7bc4\u56f2 1\uff5e10)", None))
        self.labelBoxBlenderInstalation_9.setText(QCoreApplication.translate("ConfigGUI", u"px", None))
        self.labelBoxBlenderInstalation_10.setText(QCoreApplication.translate("ConfigGUI", u"\u30ea\u30b5\u30a4\u30ba\u6bce\u52a0\u7b97\u30b5\u30a4\u30ba", None))
        self.lineEdit_resize_add_width_px.setText("")
        self.lineEdit_resize_add_width_px.setPlaceholderText(QCoreApplication.translate("ConfigGUI", u"\u6570\u5024\u3092\u5165\u529b", None))
        self.labelVersion_8.setText(QCoreApplication.translate("ConfigGUI", u"(\u7bc4\u56f2 1\uff5e999)", None))
        self.labelBoxBlenderInstalation_11.setText(QCoreApplication.translate("ConfigGUI", u"px", None))
        self.labelBoxBlenderInstalation_12.setText(QCoreApplication.translate("ConfigGUI", u"\u8abf\u6574\u7528\u52a0\u7b97\u30b5\u30a4\u30ba", None))
        self.labelVersion_9.setText(QCoreApplication.translate("ConfigGUI", u"(\u7bc4\u56f2 1\uff5e999)", None))
        self.lineEdit_adjust_width_px.setText("")
        self.lineEdit_adjust_width_px.setPlaceholderText(QCoreApplication.translate("ConfigGUI", u"\u6570\u5024\u3092\u5165\u529b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ConfigGUI", u"\u5171\u901a\u8a2d\u5b9a", None))
        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("ConfigGUI", u"\u8abf\u6574\u7528X\u5ea7\u6a19\u79fb\u52d5", None))
        self.lineEdit_adjust_x_px.setText("")
        self.lineEdit_adjust_x_px.setPlaceholderText(QCoreApplication.translate("ConfigGUI", u"\u6570\u5024\u3092\u5165\u529b", None))
        self.labelBoxBlenderInstalation_4.setText(QCoreApplication.translate("ConfigGUI", u"px", None))
        self.labelVersion_5.setText(QCoreApplication.translate("ConfigGUI", u"(\u7bc4\u56f2 1\uff5e999)", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ConfigGUI", u"\u30a6\u30a3\u30f3\u30c9\u30a6\u5de6\u914d\u7f6e", None))
        self.checkBox_windowleft_mod_ctrl.setText(QCoreApplication.translate("ConfigGUI", u"Ctrl", None))
        self.checkBox_windowleft_mod_shift.setText(QCoreApplication.translate("ConfigGUI", u"Shift", None))
        self.checkBox_windowleft_mod_alt.setText(QCoreApplication.translate("ConfigGUI", u"Alt", None))
        self.checkBox_windowleft_mod_win.setText(QCoreApplication.translate("ConfigGUI", u"Win", None))
        self.labelBoxBlenderInstalation_13.setText(QCoreApplication.translate("ConfigGUI", u"\u901a\u5e38\u30ad\u30fc", None))
        self.comboBox_Hotkey_WindowLeft.setItemText(0, QCoreApplication.translate("ConfigGUI", u"Left", None))
        self.comboBox_Hotkey_WindowLeft.setItemText(1, QCoreApplication.translate("ConfigGUI", u"Test 2", None))
        self.comboBox_Hotkey_WindowLeft.setItemText(2, QCoreApplication.translate("ConfigGUI", u"Test 3", None))

        self.groupBox_6.setTitle(QCoreApplication.translate("ConfigGUI", u"\u30a6\u30a3\u30f3\u30c9\u30a6\u53f3\u914d\u7f6e", None))
        self.checkBox_windowright_mod_ctrl.setText(QCoreApplication.translate("ConfigGUI", u"Ctrl", None))
        self.checkBox_windowright_mod_shift.setText(QCoreApplication.translate("ConfigGUI", u"Shift", None))
        self.checkBox_windowright_mod_alt.setText(QCoreApplication.translate("ConfigGUI", u"Alt", None))
        self.checkBox_windowright_mod_win.setText(QCoreApplication.translate("ConfigGUI", u"Win", None))
        self.labelBoxBlenderInstalation_14.setText(QCoreApplication.translate("ConfigGUI", u"\u901a\u5e38\u30ad\u30fc", None))
        self.comboBox_Hotkey_WindowRight.setItemText(0, QCoreApplication.translate("ConfigGUI", u"Right", None))
        self.comboBox_Hotkey_WindowRight.setItemText(1, QCoreApplication.translate("ConfigGUI", u"Test 2", None))
        self.comboBox_Hotkey_WindowRight.setItemText(2, QCoreApplication.translate("ConfigGUI", u"Test 3", None))

        self.label_settingmenu.setText(QCoreApplication.translate("ConfigGUI", u"Setting Menu", None))
        self.label_version.setText(QCoreApplication.translate("ConfigGUI", u"v4.0", None))
    # retranslateUi

