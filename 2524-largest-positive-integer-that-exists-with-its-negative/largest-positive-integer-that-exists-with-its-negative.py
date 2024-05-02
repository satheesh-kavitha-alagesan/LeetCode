class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ma = -1
        nums = set(nums)
        for n in nums:
            if n > ma and -n in nums:
                ma = n
        return ma