class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        def createChilds(val):
            res = []
            for i in range(4):
                digit = int(val[i])
                ad = str((digit + 1) %10)
                su = str(((digit - 1) +10) %10)
                res.append(val[0:i] + ad + val[i+1:])
                res.append(val[0:i] + su + val[i+1:])
            return res
        qu = deque()
        qu.append(['0000', 0])
        visited = set(deadends)
        while qu:
            val, depth = qu.popleft()
            if val == target:
                return depth
            for ch in createChilds(val):
                if ch not in visited:
                    visited.add(ch)
                    qu.append([ch, depth+1])
        return -1