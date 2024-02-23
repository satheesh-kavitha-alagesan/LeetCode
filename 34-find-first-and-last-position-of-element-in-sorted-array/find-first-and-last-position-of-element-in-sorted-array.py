class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        lb = len(nums)
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] >= target:
                lb = mid
                r = mid - 1
            else:
                l = mid + 1
        if lb >= len(nums) or nums[lb] != target:
            return [-1, -1]
        rb = len(nums)
        l = lb + 1
        r = len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] > target:
                rb = mid
                r = mid - 1
            else:
                l = mid + 1
        return [lb, rb - 1]