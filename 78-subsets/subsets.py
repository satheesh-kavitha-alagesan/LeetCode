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

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         answer = []
#         current = []
#         n = len(nums)
#         def back(index):
#             answer.append(current[:])
#             for i in range(index,n):
#                 current.append(nums[i])
#                 back(i+1)
#                 current.pop()

#         back(0)
#         return answer
        