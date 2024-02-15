class Solution:
    def intToRoman(self, num: int) -> str:
        m = {0: '', 1 : "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 500 : "D", 1000 : "M"}
        pos = 1
        st = ''
        while num>0:
            remainder = num % 10
            print("Begin : {} - {} - {} - {}".format(pos, remainder, st, num))
            if remainder == 0:
                pass
            elif remainder < 4:
                st = ''.join([m[pos] for _ in range(remainder)]) + st
            elif remainder == 4:
                st = m[pos] + m[(pos*10)/2] + st
            elif remainder == 9:
                st = m[pos] + m[pos*10] + st
            elif remainder == 5:
                st = m[pos*remainder] + st
            else:
                st = m[(pos*10)/2] + ''.join([m[pos] for _ in range(remainder-5)]) + st
            pos = pos * 10
            num = num // 10
            print("End : {} - {} - {} - {}".format(pos, remainder, st, num))
        print(st)
        return st