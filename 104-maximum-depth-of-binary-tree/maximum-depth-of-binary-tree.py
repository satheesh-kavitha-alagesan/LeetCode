# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        qu = [(root, 1)]
        ma = 0
        while qu:
            node, level = qu.pop(0)
            if node.left:
                qu.append((node.left, level+1))
            if node.right:
                qu.append((node.right, level+1))
            ma = max(level, ma)
        return ma