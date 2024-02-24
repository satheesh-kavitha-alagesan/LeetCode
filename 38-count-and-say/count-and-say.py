class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        def recur(previous):
            ma = []
            count = 1
            char = previous[0]
            for ch in previous[1::]:
                if ch == char:
                    count+=1
                else:
                    ma.append([count, char])
                    count = 1
                    char = ch
            ma.append([count, char])
            re = ''
            for k, v in ma:
                re = re+str(k)+str(v)
            return re
        previous = '11'
        for _ in range(3 ,n+1):
            previous = recur(previous)
        return previous