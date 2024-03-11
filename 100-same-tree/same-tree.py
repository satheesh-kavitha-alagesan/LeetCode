# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def rec(n1, n2):
            if ((n1 != None) and (n2 == None) or (n1 == None) and (n2 != None)):
                return False
            elif (n1 == None) and (n2 == None):
                return True
            elif n1.val == n2.val:
                return rec(n1.left, n2.left) and rec(n1.right, n2.right)
            else:
                return False
            
        return rec(p,q)