# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# #Solution 1
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ret = []
#         def rec(nd):
#             if nd is None:
#                 return
#             rec(nd.left)
#             ret.append(nd.val)
#             rec(nd.right)
#         rec(root)
#         return ret

#Solution 2
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            cur = stack.pop()
            res.append(cur.val)
            root = cur.right