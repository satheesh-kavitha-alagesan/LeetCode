class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        li = list(range(1,n+1))
        rec = set()
        temp = []
        def solve(ind):
            if len(temp) == k:
                rec.add(tuple(temp))
                return
            elif ind >= len(li):
                return
            temp.append(li[ind])
            solve(ind+1)
            temp.pop()
            solve(ind+1)
        solve(0)
        return rec