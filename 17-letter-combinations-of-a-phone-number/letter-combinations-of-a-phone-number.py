class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        ma = {'2':['a', 'b', 'c'],
        '3' :['d', 'e', 'f'],
        '4' :['g', 'h', 'i'],
        '5' :['j', 'k', 'l'],
        '6' :['m', 'n', 'o'],
        '7' :['p', 'q', 'r', 's'],
        '8' :['t', 'u', 'v'],
        '9' :['w', 'x', 'y', 'z']}
        ret = ma[digits[0]]
        digits = digits[1::]
        def recursi(aLi, bLi):
            te = []
            for _a in aLi:
                for _b in bLi:
                    te.append(_a+_b)
            return te

        for d in digits:
            ret = recursi(ret, ma[d])
        return ret