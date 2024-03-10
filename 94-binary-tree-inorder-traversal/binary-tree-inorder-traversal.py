# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def rec(nd):
            if nd is None:
                return
            rec(nd.left)
            ret.append(nd.val)
            rec(nd.right)
        rec(root)
        return ret