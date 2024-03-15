# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def rec(nd, tot):
            if not nd:
                return
            tot+= nd.val
            if (tot == targetSum) and (nd.left is None) and (nd.right is None):
                return True
            if rec(nd.left, tot):
                return True
            if rec(nd.right, tot):
                return True
        
        return rec(root, 0)