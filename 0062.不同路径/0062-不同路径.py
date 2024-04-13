class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(m,n):
            if m == 1 or n == 1:
                return 1
            return dp(m,n-1) + dp(m-1,n)
        return dp(m,n)