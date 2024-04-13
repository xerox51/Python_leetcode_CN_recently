from sortedcontainers import SortedList
class StreamRank:

    def __init__(self):
      self.num = SortedList()

    def track(self, x: int) -> None:
      self.num.add(x)

    def getRankOfNumber(self, x: int) -> int:
      return self.num.bisect_right(x)


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)