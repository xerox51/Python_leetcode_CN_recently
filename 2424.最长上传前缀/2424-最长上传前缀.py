class LUPrefix:
    def __init__(self, n: int):
        self.x = 1
        self.s = set()

    def upload(self, video: int) -> None:
        self.s.add(video)

    
    def longest(self) -> int:
        while self.x in self.s:
            self.x += 1
        return self.x - 1