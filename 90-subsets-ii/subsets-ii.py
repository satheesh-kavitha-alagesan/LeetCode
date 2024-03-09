## Solution 1
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         re = set()
#         re.add(tuple())
#         for num in nums:
#             temp = re.copy()
#             for r in re:
#                 temp.add(r+tuple([num]))
#             re = temp
#         return re

#Solution 2
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = set()
        curlist = []

        def dfs(ind):
            if ind == len(nums):
                ret.add(tuple(curlist.copy()))
                return
            curlist.append(nums[ind])
            dfs(ind+1)
            curlist.pop()
            dfs(ind+1)
        dfs(0)
        return ret