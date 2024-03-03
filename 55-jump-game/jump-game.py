class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[0] = True
        def rec(ind):
            if dp[-1]:
                return True
            for i in range(ind+1, min(ind+nums[ind]+1, len(nums))):
                if not dp[i]:
                    dp[i] = True
                    if i != ind:
                        rec(i)
        rec(0)
        return dp[-1]