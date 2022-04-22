class Counter:
    def __init__(self, base) -> None:
        self.base = base # 開始値
        self.cnt = self.base

    def increment(self, countup=1) -> None:
        self.cnt += countup

    def reset(self) -> None:
        self.cnt = self.base
    
    def get(self) -> int:
        return self.cnt
