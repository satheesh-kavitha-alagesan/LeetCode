class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        happiness = happiness[::-1]
        ret = 0
        for i in range(0,k):
            res = happiness[i] - i
            if res > 0:
                ret += res
        return ret