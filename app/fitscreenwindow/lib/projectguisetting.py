# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
# TODO:
# tk.StringVar()を使うために、親クラス(guisetting)の内部のtkを参照したいが、このimport文だと
# 子クラスで新たにインスタンス生成されているかもしれない。要確認。

import tkinter as tk

# -------------------------------------------------------------------------
# App modules
# -------------------------------------------------------------------------
from guisetting import GuiSetting

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class ProjectGuiSetting(GuiSetting):
    def __init__(self, window_title: str, favicon_path: str) -> None:
        super().__init__(window_title, favicon_path)

    # -------------------------------------------------------------------------
    # flame1
    # -------------------------------------------------------------------------
    # ラベルの表示
    def set_inputfieldflame_label1(self) -> None:
        """@override"""
        CAPTION_LABEL1 = "ウィンドウを左寄せ"
        caption: str = CAPTION_LABEL1
        label1 = self.root_ttk.Label(self.inputfieldflame, text=caption, padding=(5, 2))
        label1.grid(row=0, column=0, sticky=tk.W+tk.E)

    def create_inputfieldflame_entry1(self) -> None:
        """@override"""
        self.entry1_value = self.string_var # TODO:ここが原因かもしれない！
        val_cmd = self.root_tk.register(self.__validate_entry1)
        self.entry1_entry = self.root_ttk.Entry(
            self.inputfieldflame,
            textvariable=self.entry1_value,
            validatecommand=(val_cmd, "%d", "%i", "%P", "%s", "%S", "%v", "%V", "%W"),
            validate="all",
            width=20,
            exportselection=1,
        )
        self.entry1_entry.grid(row=0, column=1)
        
    def set_entry_value_entry1(self) -> None:
        """@override
        フィールドに初期表示させる値を定義
        """
        initial_value1 = "adfasdf"
        self.set_entry_value(self.entry1_value, initial_value1)

    def __validate_entry1(self, d, i, P, s, S, v, V, W):
        """@override"""
        print(f"{d}, {i}, {P}, {s}, {S}, {v}, {V}, {W}")
        if len(P) < 5:
            self.button1["state"] = "disabled"
        else:
            self.button1["state"] = "normal"
        return True

    # -------------------------------------------------------------------------
    # flame2
    # -------------------------------------------------------------------------
    def set_inputfieldflame_label2(self) -> None:
        """@override"""
        CAPTION_LABEL2 = "ウィンドウを右寄せ"
        caption: str = CAPTION_LABEL2
        label2 = self.root_ttk.Label(self.inputfieldflame, text=caption, padding=(5, 2))
        label2.grid(row=1, column=0, sticky=tk.W+tk.E)

    def create_inputfieldflame_entry2(self) -> None:
        """@override"""
        self.entry2_value = self.string_var # TODO:ここが原因かもしれない！
        self.entry2_entry = self.root_ttk.Entry(
            self.inputfieldflame, textvariable=self.entry2_value, width=20
        )
        self.entry2_entry.grid(row=1, column=1)

    def set_entry_value_entry2(self) -> None:
        """@override
        フィールドに初期表示させる値を定義
        """
        initial_value2 = "22222222"
        self.set_entry_value(self.entry2_value, initial_value2)

