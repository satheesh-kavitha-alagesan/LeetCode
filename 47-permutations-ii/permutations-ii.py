# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         copy = [ i for i in range(0, len(nums))]
#         ret = set()
#         def solve(arr):
#             if len(arr) == len(copy):
#                 ret.update([tuple(nums[j] for j in arr)])
#                 return
#             for i in range(0, len(copy)):
#                 if not (i in arr):
#                     arr.append(copy[i])
#                     solve(arr)
#                     arr.pop()
#         solve([])
#         ret = [list(k) for k in ret]
#         return ret

# class Solution:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         ret = []
#         mapper = [False]*len(nums)
#         arr = []
#         def solve():
#             if len(arr) == len(nums):
#                 ret.append(arr[:])
#                 return
#             used = set()
#             for i in range(len(nums)):
#                 if not mapper[i] and nums[i] not in used:
#                     mapper[i] == True
#                     arr.append(nums[i])
#                     used.add(nums[i])
#                     solve()
#                     mapper[i] = False
#                     arr.pop()
#         print(ret)
#         solve()
#         return ret

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        p = []
        v = [False] * len(nums)
        def backtrack():
            if len(p) == len(nums):
                ans.append(p[:])
                return
            used = set()
            for i in range(len(nums)):
                if not v[i] and nums[i] not in used:
                    v[i] = True
                    p.append(nums[i])
                    used.add(nums[i])
                    backtrack()
                    v[i] = False
                    p.pop()
        backtrack()
        return ans