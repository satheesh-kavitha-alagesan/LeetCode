class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = 0
        for ind in range(1, len(nums)):
            if nums[check] != nums[ind]:
                check+=1
                nums[check] = nums[ind]
        return check+1