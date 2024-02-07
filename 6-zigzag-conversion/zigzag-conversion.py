class Solution:
    def convert(self, s: str, numRows: int) -> str:
        store = {_ind:[] for _ind in range( numRows)}
        current = 0
        step = 0
        if numRows ==1:
            return s
        for st in s:
            store[current].append(st)
            if current == 0:
                step =1

            elif current == (numRows - 1):
                step = -1
            current+=step
        ret = ''.join([''.join(_l) for _, _l in store.items()])
        return ret