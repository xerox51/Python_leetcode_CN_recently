class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        res = -inf
        q = deque()
        for x, y in points:
            while q and x - q[0][1] > k:
                q.popleft()
            if q:
                res = max(res, x + y + q[0][0])
            while q and y - x >= q[-1][0]:
                q.pop()
            q.append([y - x, x])
        return res