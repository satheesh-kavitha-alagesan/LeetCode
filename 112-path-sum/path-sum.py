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

# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
#         queue = collections.deque([(root, root.val)])
#         while queue:
#             cur, pathSum = queue.popleft()
#             if not cur.left and not cur.right and pathSum == targetSum:
#                 return True
#             if cur.left:
#                 queue.append((cur.left, pathSum + cur.left.val))
#             if cur.right:
#                 queue.append((cur.right, pathSum + cur.right.val))
#         return False