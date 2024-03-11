# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(n1, n2):
            if ((n1 == None) and (n2 != None)) or ((n1 != None) and (n2 == None)):
                return False
            elif (n1 == None) and (n2 == None):
                return True
            elif n1.val != n2.val:
                return False
            else:
                return recur(n1.left, n2.right) and recur(n1.right, n2.left)
        return recur(root.left, root.right)