class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_count = {}
        for i in range(len(nums)):
            freq_count[nums[i]] = freq_count.get(nums[i], 0) + 1

        sorted_freq_count = sorted(freq_count.items(), key=lambda x: (x[1],-x[0]))
        
        nums = []
        for i in range(len(sorted_freq_count)):
            val, freq = sorted_freq_count[i]
            nums.extend([val]*freq)
        return nums