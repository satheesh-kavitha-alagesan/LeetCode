class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                val1 = 0
                val2 = 0
                if i+1 < m:
                    val1 = dp[i+1][j]
                if j+1 < n:
                    val2 = dp[i][j+1]
                dp[i][j] = dp[i][j] + val1+ val2
        return dp[0][0]