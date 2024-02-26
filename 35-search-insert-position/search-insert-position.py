class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        elif target == nums[0]:
            return 0
        left = 0
        right = len(nums) -1
        while left < right:
            mid = (right - left) // 2
            mid = left + mid
            # print(f'{left = }, {mid = }, {right =}')
            # print(f'{nums[left] = }, {nums[mid] = }, {nums[right] =}')
            if mid-1 >= 0:
                if nums[mid -1] < target < nums[mid]:
                    return mid
            if mid+1 <=len(nums)-1:
                if nums[mid] < target <= nums[mid+1]:
                    return mid + 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid