# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         ret = set()
#         le = len(candidates)
#         dp = [False]*len(candidates)
#         def solve(arr, ind):
#             print(arr)
#             if sum(arr) == target:
#                 ret.add(tuple(sorted(arr.copy())))
#                 return
#             elif sum(arr) > target:
#                 return
#             for ids, char in enumerate(candidates[ind:-1]):
#                 if not dp[ids]:
#                     dp[ids] = True
#                     arr.append(char)
#                     solve(arr, ind+1)
#                     arr.pop()
#                     dp[ids] = False
#         solve([], 0)
#         print(ret)
#         return ret

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         candidates.sort()
#         def dfs(idx, path, cur):
#             if cur > target: return
#             if cur == target:
#                 res.append(path)
#                 return
#             for i in range(idx, len(candidates)):
#                 if i > idx and candidates[i] == candidates[i-1]:
#                     continue
#                 dfs(i+1, path+[candidates[i]], cur+candidates[i])
#         dfs(0, [], 0)
#         return res

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         ds=[]
#         ans=set()
#         candidates.sort()
#         def f(i,target):
#             if i==len(candidates):
#                 if target==0:
#                     ans.add(tuple(ds))
#                 return

#             if target>=candidates[i]:
#                 ds.append(candidates[i])
#                 f(i+1,target-candidates[i])
#                 ds.pop()
#             f(i+1,target)
#         f(0,target)
#         return [list(combination) for combination in ans]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        temp = []
        ans = []
        n = len(candidates)
        def worker(idx,sumi):    
            if sumi==0:
                ans.append(temp[:])
                return
                
            if idx == n:
                return

            for i in range(idx,n):
                if i!=idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i]>sumi:
                    break
                temp.append(candidates[i])
                worker(i+1,sumi-candidates[i])
                temp.remove(candidates[i])

        worker(0,target)
        return ans                        

        