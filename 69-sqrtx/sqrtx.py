class Solution:
    def mySqrt(self, x: int) -> int:
        ret = 1
        while ret*ret <= x:
            ret +=1
        return ret -1