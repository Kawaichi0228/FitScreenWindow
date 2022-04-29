# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from pystray import Icon, MenuItem, Menu
from PIL import Image
import threading

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class Tasktray:
    def __init__(self, favicon_path, title_) -> None:
        self.favicon_path = favicon_path # ファビコン
        self.title_ = title_
        self.bind_item = [] # 右クリックで表示されるメニュー
        self.root = None
        
    def readFavicon(self) -> object:
        return Image.open(self.favicon_path)

    def addItem(self, value, on_click_function) -> None:
        self.bind_item.append(MenuItem(value, on_click_function))

    def startThread(self, favicon_obj) -> None:
        # faviconとitemをbind
        if len(self.bind_item) == 0:
            raise ValueError("タスクトレイに表示させるItemを最低1つ以上addしてください(addItemメソッド)")
        item_list = self.__getItem()
        title_ = self.title_
        self.__bindRoot(item_list, favicon_obj, title_)

        # スレッド開始
        task_thread = threading.Thread()
        task_thread.start()

        # 実行
        self.root.run()

    def stopThread(self) -> None:
        self.root.stop()

    def __bindRoot(self, item_list, favicon_path, title_) -> None:
        menu_ = Menu(*item_list) # list型に*をつけることで、リスト -> 可変長引数 へと展開する(アンパック代入)
        self.root = Icon(name=title_, title=title_, icon=favicon_path, menu=menu_)
    
    def __getItem(self) -> any:
        return self.bind_item