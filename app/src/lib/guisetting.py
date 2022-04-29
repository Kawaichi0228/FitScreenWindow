# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
import tkinter as tk

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class GuiSetting():
    def __init__(self, window_title: str, favicon_path: str) -> None:
        self.__window_title: str = window_title
        self.__favicon_path: str = favicon_path

        # tkinterオブジェクトを生成
        self.root_tk: object = None
        self.root_tk = self.new_tkinter()
        self.string_var = tk.StringVar()
        self.root_ttk = ttk

        # オブジェクト生成のメソッドからの追加用
        self.__buttons: dict = {}
        self.__entrys: dict = {}

        self.inputfieldflame: object = None
        self.__buttonflame: object = None
        self.button1: object = None
        self.button2: object = None

        self.__flameitems: dict = {}

        self.entry1_entry: object = None
        self.entry2_entry: object = None

        self.entry1_value: object = None
        self.entry2_value: object = None

    def add_buttons(self, item_dict: dict) -> None:
        """GUIに表示させる各ボタンの値と処理動作を追加"""
        self.__buttons.update(item_dict)

    def add_entrys(self, item_dict: dict) -> None:
        """Entryに追加する値と処理動作を追加"""
        self.__entrys.update(item_dict)

    def new_tkinter(self) -> object:
        tkobj = Tk()
        return tkobj

    def get_tkinter(self) -> object:
        return self.root_tk

    def start_tkinter(self, is_hidden_start: bool = False) -> None:
        """tkinterを開始"""
        # 非表示状態で開始
        if is_hidden_start:
            self.root_tk.withdraw()

        self.root_tk.mainloop()

    def stop_tkinter(self) -> None:
        """tkinterを終了"""
        self.root_tk.destroy()

    def show_gui(self) -> None:
        """ウィンドウを表示"""
        self.root_tk.deiconify()

    def hide_gui(self) -> None:
        """ウィンドウを非表示"""
        self.root_tk.withdraw()

    # ===============================================================================
    # tkinterへsetするメソッド
    # ===============================================================================
    def set_tkinter(self) -> None:
        self.__set_tkinter_mainflame()
        self.__set_tkinter_inputfieldflame()
        self.__set_tkinter_buttonflame()

    # ===============================================================================
    # Mainflameを生成
    # ===============================================================================
    def __set_tkinter_mainflame(self) -> None:
        self.__set_mainflame_windowicon(self.__favicon_path)
        self.__set_mainflame_closebutton()

    # ===============================================================================
    # Inputfieldflameを生成
    # ===============================================================================
    def __set_tkinter_inputfieldflame(self) -> None:
        self.__set_inputfieldflame_grid(self.__window_title)
        self.__set_tkinter_inputfieldflame_rows1()
        self.__set_tkinter_inputfieldflame_rows2()

    def add_items(self, item_dict: dict) -> None:
        """フレームに表示する値と処理動作を追加する"""
        self.__flameitems.update(item_dict)

    def __set_tkinter_inputfieldflame_rows1(self) -> None:
        # ラベルの表示値
        self.set_inputfieldflame_label1()

        # フレームを生成
        self.create_inputfieldflame_entry1()

        # フィールドの初期表示値
        self.set_entry_value_entry1()

    def __set_tkinter_inputfieldflame_rows2(self) -> None:
        # ラベルの表示値
        self.set_inputfieldflame_label2()

        # フレームを生成
        self.create_inputfieldflame_entry2()

        # フィールドの初期表示値
        self.set_entry_value_entry2()

    # ===============================================================================
    # Buttonflameを生成
    # ===============================================================================
    def __set_tkinter_buttonflame(self) -> None:
        self.__set_buttonflame_grid()

        CAPTION_OK_BUTTON = "設定"
        self.__set_buttonflame_okbutton(CAPTION_OK_BUTTON)

        CAPTION_CANCEL_BUTTON = "キャンセル"
        self.__set_buttonflame_cancelbutton_to_hide(CAPTION_CANCEL_BUTTON)

    # -------------------------------------------------------------------------------
    # フィールドへ値を取得or設定する
    # -------------------------------------------------------------------------------
    def __get_entry_value(self, entry_object: object) -> str:
        return entry_object.get()
    
    def set_entry_value(self, entry_value_object: object, value: str) -> str:
        return entry_value_object.set(value)

    # -------------------------------------------------------------------------------
    # InputFieldFlame
    # -------------------------------------------------------------------------------
    def __set_inputfieldflame_grid(self, title_: str) -> None:
        self.root_ttk.Style().theme_use("classic")
        self.root_tk.title(title_)
        self.root_tk.resizable(False, False)
        self.inputfieldflame = self.root_ttk.Frame(self.root_tk, padding=(32))
        self.inputfieldflame.grid()

    def set_inputfieldflame_label1(self) -> None:
        """override用メソッド"""
        pass

    def create_inputfieldflame_entry1(self) -> None:
        """override用メソッド"""
        pass

    def set_entry_value_entry1(self) -> None:
        """override用メソッド"""
        pass

    def set_inputfieldflame_label2(self) -> None:
        """override用メソッド"""
        pass

    def create_inputfieldflame_entry2(self) -> None:
        """override用メソッド"""
        pass

    def set_entry_value_entry2(self) -> None:
        """override用メソッド"""
        pass

    # -------------------------------------------------------------------------------
    # ButtonFlame
    # -------------------------------------------------------------------------------
    def __set_buttonflame_grid(self) -> None:
        self.__buttonflame = self.root_ttk.Frame(self.inputfieldflame, padding=(0, 5))
        self.__buttonflame.grid(row=2, column=1, sticky=W)

    def __set_buttonflame_okbutton(self, caption: str) -> None:
        self.button1 = self.root_ttk.Button(
            self.__buttonflame,
            text=caption,
            state="disabled",
            # MEMO:lambdaで処理を入れないと画面表示されなくなるので注意
            command=lambda: self.__process_okbutton(),
        )
        self.button1.pack(side=LEFT)

    def __set_buttonflame_cancelbutton_to_hide(self, caption: str) -> None:
        """ボタンクリック後にtkinterを非表示"""
        # tkinterを非表示
        self.button2 = self.root_ttk.Button(
            self.__buttonflame, text=caption, command=lambda: self.hide_gui()
        )

        # buttonをpack
        self.button2.pack(side=LEFT)

    def __set_buttonflame_cancelbutton_to_quit(self, caption: str) -> None:
        """ボタンクリック後にtkinterを終了"""
        # tkinterを終了
        self.button2 = self.root_ttk.Button(self.__buttonflame, text=caption, command=quit)

        # buttonをpack
        self.button2.pack(side=LEFT)

    def __process_okbutton(self) -> None:
        print("フィールド1の入力値", self.__get_entry_value(self.entry1_entry))
        print("フィールド2の入力値", self.__get_entry_value(self.entry2_entry))
        self.hide_gui()
        print("%s,%s" % (self.entry1_value.get(), self.entry2_value.get()))

    # -------------------------------------------------------------------------------
    # mainflame
    # -------------------------------------------------------------------------------
    def __set_mainflame_windowicon(self, icon_path: str) -> None:
        """guiウィンドウのアイコンをセット"""
        self.root_tk.iconbitmap(icon_path)

    def __set_mainflame_closebutton(self) -> None:
        """Xボタンが押された時の処理をセット"""
        # Xボタンが押下されたらguiを非表示にする
        self.root_tk.protocol("WM_DELETE_WINDOW", lambda: self.hide_gui())

    # -------------------------------------------------------------------------------
    # Main
    # -------------------------------------------------------------------------------
    def main(self, is_hidden_start: bool) -> None:
        self.set_tkinter()
        self.start_tkinter(is_hidden_start)
