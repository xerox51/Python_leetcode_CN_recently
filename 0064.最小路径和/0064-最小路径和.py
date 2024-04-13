class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        grid_r = [[row[i] for row in grid] for i in range(len(grid[0]))]
        @cache
        def dp(m,n):
            if m == 0:
               return sum(grid[0][0:n+1])
            if n == 0:
               return sum(grid_r[0][0:m+1])
            return min(dp(m,n-1) + grid[m][n],dp(m-1,n) + grid[m][n])
        return dp(len(grid) - 1,len(grid[0]) - 1)