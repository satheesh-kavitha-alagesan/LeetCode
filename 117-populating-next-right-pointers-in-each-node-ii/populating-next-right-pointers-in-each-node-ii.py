"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = []

        q.append(root)
        while q:
            level = q.copy()
            q.clear()

            for i in range(0, len(level)):
                if level[i] is None:
                    continue
                    
                if i == len(level)-1:
                    level[i].next = None
                else:
                    level[i].next = level[i+1]
                
                if level[i].left:
                    q.append(level[i].left)
                if level[i].right:
                    q.append(level[i].right)
        return root