class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        maps = defaultdict(list)
        for num in nums:
            cp = num
            finalNum = 0
            mu = 1
            if num == 0:
                maps[mapping[0]].append(cp)
                continue
            while num > 0:
                rem = num %10
                num //= 10
                finalNum += mapping[rem] * mu
                mu *=10
            maps[int(finalNum)].append(cp)
        ret = []
        for _k in sorted(maps.keys()):
            ret.extend(maps[_k])
        return ret