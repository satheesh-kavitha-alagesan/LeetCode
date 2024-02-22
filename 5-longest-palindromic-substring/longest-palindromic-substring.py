class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) <= 1:
        #     return s
        
        # Max_Len=1
        # Max_Str=s[0]
        # dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        # for i in range(len(s)):
        #     dp[i][i] = True
        #     for j in range(i):
        #         if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
        #             dp[j][i] = True
        #             if i-j+1 > Max_Len:
        #                 Max_Len = i-j+1
        #                 Max_Str = s[j:i+1]
        # return Max_Str

        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i-dp[i]:i+dp[i]+1].replace('#','')
        return Max_Str