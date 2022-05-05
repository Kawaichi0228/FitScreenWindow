# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
import json

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class JsonController:
    """jsonファイルの読み込み & 書き込み などを行うクラス"""
    def __init__(self, json_path: str) -> None:
        self.__json_path = json_path

    def read(self) -> object:
        """Fileオブジェクトを読み込み生成(Create Object)"""
        json_obj = open(self.__json_path, "r", encoding="utf-8") # 'r'はread
        return json_obj
    
    def getDictionary(self, json_obj) -> dict:
        """jsonファイルの内容を、dictionaryとして取得"""
        json_dict = json.load(json_obj)
        return json_dict

    def save(self, json_dict: dict, indent_space: int=4) -> None:
        """
        書き換える値が格納されたリストを渡して、jsonを上書き保存する
        MEMO: 指定パスのファイルが存在しない場合は新規作成される(エラーは出ない)
        """
        with open(self.__json_path, "w", encoding="utf-8") as js: # 'w'はwrite
            json.dump(
                json_dict, js, indent=indent_space, ensure_ascii=False
            )  # ensure_ascii:Falseで日本語がUnicode変換されないようにする
