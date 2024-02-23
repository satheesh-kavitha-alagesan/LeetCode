class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(dividend) == abs(divisor):
            val = 1
        elif abs(divisor) in (1, -1):
            val = abs(dividend)
        else:
            val = len(range(0, abs(dividend)-abs(divisor)+1, abs(divisor)))
        if dividend < 0 and divisor < 0:
            val = val
        elif dividend < 0 or divisor < 0:
            val = -val
        print(val)
        if val > 2**31 - 1:
            return 2**31 - 1
        elif val < -2**31:
            return 2**31
        return val