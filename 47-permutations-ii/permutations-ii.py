class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        copy = [ i for i in range(0, len(nums))]
        ret = set()
        def solve(arr):
            if len(arr) == len(copy):
                ret.update([tuple(nums[j] for j in arr)])
                return
            for i in range(0, len(copy)):
                if not (i in arr):
                    arr.append(copy[i])
                    solve(arr)
                    arr.pop()
        solve([])
        ret = [list(k) for k in ret]
        return ret