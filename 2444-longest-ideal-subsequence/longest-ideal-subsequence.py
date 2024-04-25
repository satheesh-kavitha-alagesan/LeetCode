class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 27
        for i in range(len(s) - 1, -1, -1):
            idx = ord(s[i]) - ord('a')
            dp[idx] = max(0, max(dp[max((idx - k), 0): min((idx + k), 26) + 1])) +1
        return max(dp)