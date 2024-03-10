# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         def po(a, b):
#             ret = 1
#             for _ in range(b):
#                 ret *= a
#             return ret
#         if n >= 0:
#             return po(x,n)
#         else:
#             return 1/po(x, abs(n))

class Solution:
    def solve(self, x, n):
        ans = 1
        while n > 0:
            if n & 1:  # checking if it is odd then we will multiply one extra value of x
                ans *= x
            x *= x
            n >>= 1
        return ans
    
    def myPow(self, x: float, n: int) -> float:
        if x == 1:
            return 1
        long_n = abs(n)
        ans = self.solve(x, long_n)
        if n < 0:
            return 1 / ans
        return ans
