class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ret = 0
        while ret < len(nums):
            if ret + 2 < len(nums):
                if nums[ret] == nums[ret+2]:
                    nums.pop(ret+2)
                    ret -= 1
            ret += 1
        return ret