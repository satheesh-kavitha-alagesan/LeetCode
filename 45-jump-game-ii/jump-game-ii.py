class Solution:
    # def jump(self, nums):
    #     if len(nums) <= 1: return 0
    #     l, r = 0, nums[0]
    #     times = 1
    #     while r < len(nums) - 1:
    #         times += 1
    #         nxt = max(i + nums[i] for i in range(l, r + 1))
    #         l, r = r, nxt
    #     return times


    def jump(self, nums):
        le = len(nums)
        dp = [le for _ in range(len(nums))]
        dp[0] = 0
        for ind, num in enumerate(nums):
            for slide in range(1,num+1):
                if ind+slide < le:
                    dp[ind+slide] = min(dp[ind+slide], dp[ind] + 1)
        return dp[-1]