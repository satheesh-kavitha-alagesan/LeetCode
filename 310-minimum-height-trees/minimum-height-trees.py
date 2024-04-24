
# Time Complex solution
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         if not edges:
#             return [0]
#         dd = defaultdict(list)
#         mindp = float('inf')
#         ret = []
#         for le, re in edges:
#             dd[le].append(re)
#             dd[re].append(le)

#         def rec(used, dep, q):
#             nq = deque()
#             while q:
#                 cur = q.popleft()
#                 for k in dd[cur]:
#                     if not k in used:
#                         used.add(k)
#                         nq.append(k)
#             if nq:
#                 return rec(used, dep+1, nq)
#             else:
#                 return dep

#         for key in dd.keys():
#             used = set()
#             used.add(key)
#             q = deque()
#             q.append(key)
#             cudp = rec(used, 1, q)
#             if cudp < mindp:
#                 mindp = cudp
#                 ret = [key]
#             elif cudp == mindp:
#                 ret.append(key)
#         return ret

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        counts = [0] * n
        links = [0] * n
        
        for edge in edges:
            links[edge[0]] ^= edge[1]
            counts[edge[0]] += 1
            links[edge[1]] ^= edge[0]
            counts[edge[1]] += 1
        
        Qu = deque()
        dists = [0] * n
        
        for i in range(n):
            if counts[i] == 1:
                Qu.append(i)
        
        stp = 1
        while Qu:
            size = len(Qu)
            for _ in range(size):
                tmp = Qu.popleft()
                links[links[tmp]] ^= tmp
                counts[links[tmp]] -= 1
                if counts[links[tmp]] == 1:
                    dists[links[tmp]] = max(stp, dists[links[tmp]])
                    Qu.append(links[tmp])
            stp += 1
        
        max_dist = max(dists)
        res = [i for i in range(n) if dists[i] == max_dist]
        
        return res
