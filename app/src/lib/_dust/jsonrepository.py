# -------------------------------------------------------------------------
# Python modules
# -------------------------------------------------------------------------
from abc import ABC, abstractclassmethod

# -------------------------------------------------------------------------
# Class
# -------------------------------------------------------------------------
class JsonRepository:
    def __init__(self) -> None:
        pass

    def defineConfig(self) -> dict:
        """MEMO: 必ずdictの中身をconfig.jsonを全て一致させておくこと(まるごとjsonコピペでよい)"""
        config_dict = {
            "size": {
                "resize_max_cnt": ValidateInt(1,10),
                "resize_add_width_px": ValidateInt(1,10),
                "base_width_toleft_px": ValidateInt(1,2000),
                "base_width_toright_px": ValidateInt(1,2000),
                "adjust_width_px": ValidateInt(1,100)
            },
            "position": {
                "adjust_x_px": ValidateInt(1,100)
            },
            "hotkey_windowleft": {
                "mod_ctrl": ValidateBool(),
                "mod_shift": ValidateBool(),
                "mod_alt": ValidateBool(),
                "hotkey": "g" # TODO: キーリストのclass作成
            },
            "hotkey_windowright": {
                "mod_ctrl": ValidateBool(),
                "mod_shift": ValidateBool(),
                "mod_alt": ValidateBool(),
                "hotkey": "h" # TODO: キーリストのclass作成
            }
        }
        return config_dict

class IValidate(ABC):
    @abstractclassmethod
    def __init__(self) -> None: pass
    @abstractclassmethod
    def isValid(self, num) -> bool: pass

class ValidateBool(IValidate):
    def __init__(self) -> None:
        pass

    def isValid(self, num) -> bool:
        return True if num == 0 or num == 1 else False

class ValidateInt(IValidate):
    def __init__(self, min, max) -> None:
        self.min = min
        self.max = max

    def isValid(self, num) -> bool:
        return True if self.min <= num <= self.max else False

class ValidateHotKey(IValidate):
    def __init__(self) -> None:
        pass

    def isValid(self, num) -> bool:
        pass


if __name__ == "__main__":
    json = JsonRepository()
    config_dict = json.defineConfig()
    config_list = list(config_dict.items())
    
    # validateクラスを取り出す前準備
    value_dict = []
    for i in range(0,len(config_list),1):
        value_dict.append(config_list[i][1].values()) # [n][x]のnには二次元目がクラスが格納されている

    # validateクラスを取り出す
    for i in range(0,len(value_dict),1):
        for cls_validate in value_dict[i]:
            print(cls_validate)
            c = cls_validate(50)
            c.isValid(500)
    
