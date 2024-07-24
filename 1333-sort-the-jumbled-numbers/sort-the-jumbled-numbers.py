class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        maps = defaultdict(list)
        for num in nums:
            finalNum = ''
            for dig in str(num):
                finalNum += str(mapping[int(dig)])
            maps[int(finalNum)].append(num)
        ret = []
        for _k in sorted(maps.keys()):
            ret.extend(maps[_k])
        return ret