# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def validate(node, valrange = (float('-inf'), float('inf'))):
#             if node.left:
#                 if valrange[0] < node.left.val < node.val < valrange[1]:
#                     return validate(node.left, (valrange[0], node.val))
#                 else:
#                     return False
#             if node.right:
#                 if valrange[0] < node.val < node.right.val < valrange[1]:
#                     return validate(node.right, (node.val, valrange[1]))
#                 else:
#                     return False
#             left = []
#             return True
#         return validate(root)

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         prev = float('-inf')
#         def inorder(node):
#             nonlocal prev
#             if not node:
#                 return True
#             if not (inorder(node.left) and prev < node.val):
#                 return False
#             prev = node.val
#             return inorder(node.right)
#         return inorder(root)


class Solution:
    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        if not root:
            return True
        if root.val >= ceiling or root.val <= floor:
            return False 
        return self.isValidBST(root.left, floor, min(ceiling, root.val)) and \
               self. isValidBST(root.right, max(floor, root.val), ceiling)
