class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for _outIndex in range(0,len(nums)):
        #     for _innerIndex in range(_outIndex+1, len(nums)):
        #         if nums[_outIndex] + nums[_innerIndex] == target:
        #             return [_outIndex, _innerIndex]
        # numsDict = {}
        
        # for _i in nums:
        #     if _i in numsDict.keys():
        #         numsDict[_i] = numsDict[_i] + 1
        #     else:
        #         numsDict[_i] = 1
        
        # for _k in numsDict.keys():
        #     if (target - _k) in numsDict.keys() and (target - _k) != _k:
        #         return [nums.index(_k), nums.index(target - _k)]
        #     elif (target - _k) in numsDict.keys() and (target - _k) == _k:
        #         if numsDict[_k] > 1:
        #             return [nums.index(_k), nums.index(_k, nums.index(_k)+1)]

        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i