from collections import deque, defaultdict
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        ed = defaultdict(list)
        qu = deque()
        for key, val in edges:
            ed[key].append(val)
            ed[val].append(key)
        
        qu.append(1)
        res = -1
        cur_time = 0
        visit_times = defaultdict(list)
        while qu:
            for _ in range(len(qu)):
                nd = qu.popleft()
                if nd == n:
                    if res != -1:
                        return cur_time
                    res = cur_time
                for nei in ed[nd]:
                    nei_times = visit_times[nei]
                    if len(nei_times) == 0 or (len(nei_times) == 1 and nei_times[0] != cur_time):
                        qu.append(nei)
                        nei_times.append(cur_time)
            if (cur_time // change) % 2 ==1:
                cur_time += change - (cur_time%change)
            cur_time+= time