class Solution:
    def nextPermutation(self, nums) -> None:
        found = False
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                nums[i:] = nums[i:][::-1]
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                found = True
                break
        if not found: nums.reverse()