class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp = [False]*len(nums)
        # dp[0] = True
        # def rec(ind):
        #     if dp[-1]:
        #         return True
        #     for i in range(ind+1, min(ind+nums[ind]+1, len(nums))):
        #         if not dp[i]:
        #             dp[i] = True
        #             if i != ind:
        #                 rec(i)
        # rec(0)
        # return dp[-1]

        target = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i]>= target:
                target = i
        return not target
