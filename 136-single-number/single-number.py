class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        di = defaultdict(int)
        for val in nums:
            di[val] = di[val]+1
            if di[val] == 2:
                del di[val]
        return list(di.keys())[0]