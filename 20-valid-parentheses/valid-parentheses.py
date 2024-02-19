class Solution:
    def isValid(self, s: str) -> bool:
        li = []
        opMap = {')' : '(', '}' : '{', ']' : '[' }
        for ch in s:
            if len(li) > 0:
                if li[-1] == opMap.get(ch, False):
                    li.pop(-1)
                else:
                    li.append(ch)
            else:
                li.append(ch)
        return li == []