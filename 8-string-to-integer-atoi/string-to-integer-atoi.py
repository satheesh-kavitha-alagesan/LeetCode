class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        negativeFlag = False
        if s.startswith('-'):
            negativeFlag = True
            s=s[1::]
        elif s.startswith('+'):
            s=s[1::]
        num = 0
        x = lambda y : y - (y+y) if negativeFlag else y
        for c in s:
            if c.isdigit():
                num = (num*10) + int(c)
            else:
                return x(num)
            if (2147483648 <= num) and negativeFlag:
                return -2147483648
            elif (2147483647 <= num) and (not negativeFlag):
                return 2147483647
        return x(num)