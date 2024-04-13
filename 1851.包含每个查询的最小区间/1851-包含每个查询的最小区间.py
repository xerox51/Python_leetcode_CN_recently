class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        qindex = list(range(len(queries)))
        qindex.sort(key=lambda i: queries[i])
        intervals.sort(key=lambda i: i[0])
        pq = []
        res = [-1] * len(queries)
        i = 0
        for qi in qindex:
            while i < len(intervals) and intervals[i][0] <= queries[qi]:
                heappush(pq, (intervals[i][1] - intervals[i][0] + 1, intervals[i][0], intervals[i][1]))
                i += 1
            while pq and pq[0][2] < queries[qi]:
                heappop(pq)
            if pq:
                res[qi] = pq[0][0]
        return res