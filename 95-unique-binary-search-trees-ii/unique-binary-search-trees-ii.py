# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}  
        def generate(left, right):
            if (left, right) in dp:
                return dp[(left, right)]
            if left == right:
                return [TreeNode(left)]
            if left > right:
                return [None]
            ret = []
            for val in range(left, right+1):
                for leftNode in generate(left, val-1):
                    for rightNode in generate(val+1, right):
                        ret.append(TreeNode(val, leftNode, rightNode))
            dp[(left, right)] = ret
            return ret
        return generate(1, n)