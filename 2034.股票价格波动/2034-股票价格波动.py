from sortedcontainers import SortedDict,SortedList
class StockPrice:

    def __init__(self):
      self.h = SortedDict()
      self.n = SortedList()
    def update(self, timestamp: int, price: int) -> None:
      if timestamp in self.h.keys():
        self.n.discard(self.h[timestamp])
        self.n.add(price)
        self.h[timestamp] = price
      else:
        self.h[timestamp] = price
        self.n.add(price)
    def current(self) -> int:
      return self.h[self.h.keys()[-1]]
    def maximum(self) -> int:
      return self.n[-1]
    def minimum(self) -> int:
      return self.n[0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()