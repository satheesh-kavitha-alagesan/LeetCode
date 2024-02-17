class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # retList = []
        # nums = sorted(nums)
        # for oind, o in enumerate(nums):
        #     for iind, i in enumerate(nums):
        #         if oind != iind:
        #             remain = 0 - (o+i)
        #             for jind, j in enumerate(nums):
        #                 if (j == remain) and (jind != oind) and (jind != iind):
        #                     valList = sorted([nums[oind],nums[iind],nums[jind]])
        #                     if valList not in retList:
        #                         retList.append(valList)
        # return retList

        # nums.sort()
        # answer = []

        # if len(nums) < 3:
        #     return answer

        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         break

        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue

        #     low, high = i + 1, len(nums) - 1
        #     while low < high:
        #         s = nums[i] + nums[low] + nums[high]
        #         if s > 0:
        #             high -= 1
        #         elif s < 0:
        #             low += 1
        #         else:
        #             answer.append([nums[i], nums[low], nums[high]])
        #             lastLowOccurrence, lastHighOccurrence = nums[low], nums[high]

        #             while low < high and nums[low] == lastLowOccurrence:
        #                 low += 1

        #             while low < high and nums[high] == lastHighOccurrence:
        #                 high -= 1

        # return answer
        nums.sort()
        ret = []
        print(nums)
        for ind in range(len(nums)):
            if nums[ind] > 0:
                break
            if ind > 0 and (nums[ind] == nums[ind-1]):
                continue
            start = ind + 1
            end = len(nums) - 1
            remaining = 0 - nums[ind]
            while start < end:
                tot = nums[start] + nums[end]
                if tot == remaining:
                    ap = [nums[ind], nums[start], nums[end]]
                    ret.append(ap)
                    lastLowOccurrence, lastHighOccurrence = nums[start], nums[end]
                    while start < end and nums[start] == lastLowOccurrence:
                        start += 1

                    while start < end and nums[end] == lastHighOccurrence:
                        end -= 1
                elif tot > remaining:
                    end -= 1
                elif tot < remaining:
                    start += 1
        return ret
