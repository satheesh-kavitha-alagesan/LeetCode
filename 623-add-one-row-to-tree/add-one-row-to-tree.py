# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # if depth == 1:
        #     return TreeNode(val, left = root)
        def rec(node, stage, side = 'l'):
            if stage == depth:
                if side == 'l':
                    return TreeNode(val, left = node)
                else:
                    return TreeNode(val, right = node)
            else:
                if node.left or (stage+1 == depth):
                    node.left = rec(node.left, stage+1, side = 'l')
                if node.right or (stage+1 == depth):
                    node.right = rec(node.right, stage+1, side = 'r')
                return node
        return rec(root, 1, side = 'l')