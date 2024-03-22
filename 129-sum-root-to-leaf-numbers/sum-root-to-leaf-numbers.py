# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if node.left:
                li1 = rec(node.left)
            else:
                li1 = []
            if node.right:
                li2 = rec(node.right)
            else:
                li2 = []
            if (not node.left) and (not node.right):
                return [str(node.val)]
            else:
                li1 = [str(node.val)+i  for i in li1]
                li2 = [str(node.val)+i  for i in li2]
                return li1+li2
        vals = rec(root)
        ret = 0
        for val in vals:
            ret += int(val)
        return ret