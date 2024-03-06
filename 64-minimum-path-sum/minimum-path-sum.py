class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*n for _ in range(m)]

        for i in range(0,m):
            for j in range(0,n):
                val1 = grid[i][j]
                val2 = grid[i][j]
                if (i-1 >= 0) and (j-1 >= 0):
                    dp[i][j] = min((grid[i][j] + dp[i-1][j]) , (grid[i][j] + dp[i][j-1]))
                elif (i-1 < 0) and (j-1 < 0):
                    dp[i][j] = grid[i][j]
                elif i-1 >= 0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                elif j-1 >= 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                
        # for k in dp:
        #     print(k)
        
        return dp[m-1][n-1]