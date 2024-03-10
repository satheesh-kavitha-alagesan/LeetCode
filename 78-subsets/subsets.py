class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        temp = []
        def dfs(ind):
            ret.add(tuple(temp))
            if ind >= len(nums):
                return
            temp.append(nums[ind])
            dfs(ind+1)
            temp.pop()
            dfs(ind+1)
        dfs(0)
        return ret
