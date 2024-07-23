class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency_map = Counter(nums)
    
        return sorted(nums, key=lambda x: (frequency_map[x], -x))