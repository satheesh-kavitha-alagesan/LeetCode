class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[-1]*n for _ in range(m)]
        def rec(i, j, s1, s2):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s1[i] == s2[j]:
                dp[i][j] = rec(i-1, j-1, s1, s2)
                return dp[i][j]
            else:
                dp[i][j] = 1+ min(rec(i-1, j, s1, s2), min(rec(i, j-1, s1, s2), rec(i-1, j-1, s1, s2)))
                return dp[i][j]
        ret = rec(m-1, n-1, word1, word2)
        return ret