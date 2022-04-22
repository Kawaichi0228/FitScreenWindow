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
        self.__json_object = self.__createObject(self.__json_path)
        self.__json_dict = {}

    def __del__(self) -> None:
        self.__deleteObject(self.__json_object)

    def getDictionary(self) -> dict:
        """jsonファイルの内容を、dictionaryとして取得"""
        self.__json_dict = json.load(self.__json_object)
        jsonDict = self.__json_dict
        return jsonDict

    def overWriteSave(self, json_dict: dict, indentSpace: int = 4) -> None:
        """書き換える値が格納されたリストを渡して、jsonを上書き保存する"""
        with open(self.__json_path, "w", encoding="utf-8") as js: # 'w'はwrite
            json.dump(
                json_dict, js, indent=indentSpace, ensure_ascii=False
            )  # ensure_ascii:Falseで日本語がUnicode変換されないようにする\

    def __createObject(self, json_path: str) -> object:
        """Fileオブジェクトを生成"""
        obj = open(json_path, "r")  # 'r'はread
        return obj

    def __deleteObject(self, json_obj: object) -> None:
        """Fileオブジェクトを閉じる"""
        json_obj.close()
