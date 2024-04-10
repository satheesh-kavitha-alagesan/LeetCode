class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for n in range(1, (10**5)+2):
            if not nums.get(n, None):
                return n