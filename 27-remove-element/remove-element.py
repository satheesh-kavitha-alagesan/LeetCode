class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        nums.append('-')
        while True:
            if nums[count] == val:
                nums.append(nums.pop(count))
                continue
            elif nums[count] == '-':
                return count
            else:
                count+=1