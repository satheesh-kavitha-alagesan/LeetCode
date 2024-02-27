# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def rec(l1, l2):
#             lr = []
#             for l2e in l2:
#                 for l1e in l1:
#                     if l2e not in l1e:
#                         lr.append(l1e + [l2e])
#             return lr
#         l1 = [[n] for n in nums]
#         for _ in range(len(nums) -1):
#             l1 = rec(l1, nums)
#         return l1

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(i,temp):
            if i >= len(nums):
                res.append(temp.copy())
                return
            for j in range(len(nums)):
                if nums[j] not in temp:
                    temp.append(nums[j])
                    solve(i+1,temp)
                    temp.pop()
            # return 
        solve(0,[])
        return res