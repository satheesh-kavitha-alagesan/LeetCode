# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         l = 0
#         r = len(nums) - 1
#         lb = len(nums)
#         while l <= r:
#             mid = (l+r) // 2
#             if nums[mid] >= target:
#                 lb = mid
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         if lb >= len(nums) or nums[lb] != target:
#             return [-1, -1]
#         rb = len(nums)
#         l = lb + 1
#         r = len(nums) - 1
#         while l <= r:
#             mid = (l+r) // 2
#             if nums[mid] > target:
#                 rb = mid
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return [lb, rb - 1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        first, last = -1, -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first, last = mid, mid
                while first > 0 and nums[first-1] == target:
                    first -= 1
                while last < len(nums)-1 and nums[last+1] == target:
                    last += 1
                return [first, last]

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1    
        
        return [first, last]