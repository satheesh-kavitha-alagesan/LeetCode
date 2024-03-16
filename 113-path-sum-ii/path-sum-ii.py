# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ret = []
        def rec(node, li):
            li.append(node.val)
            if (sum(li) == targetSum) and (node.left is None) and (node.right is None):
                ret.append(li)
                return 
            if node.left:
                rec(node.left, li[:])
            if node.right:
                rec(node.right, li[:])
        rec(root, [])
        return ret