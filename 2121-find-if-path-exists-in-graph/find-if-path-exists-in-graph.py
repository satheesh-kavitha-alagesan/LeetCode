class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for e1,e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for nd in graph[node]:
                if not nd in visited:
                    if dfs(nd, visited):
                        return True
            return False
        return dfs(source, set())