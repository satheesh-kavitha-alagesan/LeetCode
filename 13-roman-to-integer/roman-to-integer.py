class Solution:
    def romanToInt(self, s: str) -> int:
        # m = {"I" : 1, "IV" : 4, "V" : 5, "IX" : 9, "X" : 10, "XL" : 40, "L" : 50, "XC" : 90 , "C" : 100, "CD" : 400, "D" : 500, "CM" : 900, "M" : 1000}
        # passFlag = False
        # num = 0
        # for ind in range(len(s)):
        #     if passFlag:
        #         passFlag = False
        #         continue
        #     if ind+1 < len(s):
        #         if (s[ind] + s[ind+1]) in m.keys():
        #             num += m[s[ind] + s[ind+1]]
        #             passFlag = True
        #         else:
        #             num += m[s[ind]]
        #     else:
        #         num += m[s[ind]]
        # return num

        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        number=0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[(i+1)]]:
                number-=roman[s[i]]
            else:
                number+=roman[s[i]]
        return number+roman[s[-1]]