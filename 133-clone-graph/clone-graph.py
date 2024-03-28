"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]


# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         def dfs(cur_node):
#             if not cur_node:
#                 return None
#             orig_copy_nodes_list[ cur_node.val ] = Node(val = cur_node.val)
#             for neighbour in cur_node.neighbors:
#                 if orig_copy_nodes_list[ neighbour.val ] != None:
#                     pass
#                 if orig_copy_nodes_list[ neighbour.val ] == None:
#                     dfs(neighbour)
#                 orig_copy_nodes_list[ cur_node.val ].neighbors.append(orig_copy_nodes_list[ neighbour.val ])
#         orig_copy_nodes_list = [ None ]
#         if not node:
#             return None
#         dfs(node)
#         return orig_copy_nodes_list[ node.val ]