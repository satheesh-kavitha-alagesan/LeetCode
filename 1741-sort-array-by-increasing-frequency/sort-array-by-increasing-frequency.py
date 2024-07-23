from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numCountMapping = defaultdict(int)
        for _num in nums :
            numCountMapping[_num] += 1
        countValMap = defaultdict(list)
        for _k, _v in numCountMapping.items():
            countValMap[_v].append(_k)
        res = []
        for occur in sorted(list(countValMap.keys())):
            for num in sorted(countValMap[occur], reverse = True): 
                res.extend([num]*occur)
        return res