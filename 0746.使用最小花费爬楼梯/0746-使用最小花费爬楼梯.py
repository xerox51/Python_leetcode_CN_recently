class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(n):
          if n == 0 or n == 1:
            return 0
          else:
            return min(dp(n-1)+cost[n-1],cost[n-2] + dp(n-2))

        return dp(len(cost))