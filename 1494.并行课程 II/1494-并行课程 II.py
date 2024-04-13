class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        dp = [inf] * (1 << n)
        need = [0] * (1 << n)
        for edge in relations:
            need[(1 << (edge[1] - 1))] |= 1 << (edge[0] - 1)
        dp[0] = 0
        for i in range(1, (1 << n)):
            need[i] = need[i & (i - 1)] | need[i & (-i)]
            if (need[i] | i) != i:
                continue
            sub = valid = i ^ need[i]
            if sub.bit_count() <= k:
                dp[i] = min(dp[i], dp[i ^ sub] + 1)
            else:
                while sub:
                    if sub.bit_count() <= k:
                        dp[i] = min(dp[i], dp[i ^ sub] + 1)
                    sub = (sub - 1) & valid
        return dp[-1]