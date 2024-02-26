class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ma = {'0' : 0 , '1': 1, '2' : 2, '3' : 3 , '4' : 4 , '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9 }
        def func(num):
            ret = 0
            mult = 1
            while num:
                ret+=ma[num[-1]]*mult
                num = num[:-1]
                mult *= 10
            return ret
        r1 = func(num1)
        r2 = func(num2)
        print(r1, r2)
        return  str(r1*r2)