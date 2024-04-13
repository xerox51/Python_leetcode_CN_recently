class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.min = [0] * (n * 4)
        self.sum = [0] * (n * 4)

    
    def add(self, o: int, l: int, r: int, idx: int, val: int):
        if l == r:
            self.min[o] += val
            self.sum[o] += val
            return
        m = (l + r) // 2
        if idx <= m: self.add(o * 2, l, m, idx, val)
        else: self.add(o * 2 + 1, m + 1, r, idx, val)
        self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]

    
    def query_sum(self, o: int, l: int, r: int, L: int, R: int):
        if L <= l and r <= R: return self.sum[o]
        sum = 0
        m = (l + r) // 2
        if L <= m: sum += self.query_sum(o * 2, l, m, L, R)
        if R > m: sum += self.query_sum(o * 2 + 1, m + 1, r, L, R)
        return sum

    
    def index(self, o: int, l: int, r: int, R: int, val: int):
        if self.min[o] > val: return 0  
        if l == r: return l
        m = (l + r) // 2
        if self.min[o * 2] <= val: return self.index(o * 2, l, m, R, val)  
        if m < R: return self.index(o * 2 + 1, m + 1, r, R, val)  
        return 0

    def gather(self, k: int, maxRow: int) -> List[int]:
        i = self.index(1, 1, self.n, maxRow + 1, self.m - k)
        if i == 0: return []
        seats = self.query_sum(1, 1, self.n, i, i)
        self.add(1, 1, self.n, i, k)  
        return [i - 1, seats]

    def scatter(self, k: int, maxRow: int) -> bool:
        if (maxRow + 1) * self.m - self.query_sum(1, 1, self.n, 1, maxRow + 1) < k:
            return False  
        i = self.index(1, 1, self.n, maxRow + 1, self.m - 1)  
        while True:
            left_seats = self.m - self.query_sum(1, 1, self.n, i, i)
            if k <= left_seats:  
                self.add(1, 1, self.n, i, k)
                return True
            k -= left_seats
            self.add(1, 1, self.n, i, left_seats)
            i += 1