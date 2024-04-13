class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.sum = [0]
        for a, b, x, y in rects:
            self.sum.append(self.sum[-1] + (x - a + 1) * (y - b + 1))
        print(self.sum)

    def pick(self) -> List[int]:
        k = randrange(self.sum[-1])
        rectIndex = bisect_right(self.sum, k) - 1
        a, b, _, y = self.rects[rectIndex]
        da, db = divmod(k - self.sum[rectIndex], y - b + 1)
        return [a + da, b + db]