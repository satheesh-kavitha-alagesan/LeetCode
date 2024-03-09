class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        re = set()
        re.add(tuple())
        for num in nums:
            temp = re.copy()
            for r in re:
                temp.add(r+tuple([num]))
            re = temp
        return re

# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         re = set()
#         re.add(tuple())
#         for num in range(len(nums)):
#             temp = re.copy()
#             for r in re:
#                 temp.add(r+tuple([num]))
#             re = temp
#         ret = []
#         for l in re:
#             temp = []
#             for i in l:
#                 temp.append(nums[i])
#             ret.append(temp)

#         return ret