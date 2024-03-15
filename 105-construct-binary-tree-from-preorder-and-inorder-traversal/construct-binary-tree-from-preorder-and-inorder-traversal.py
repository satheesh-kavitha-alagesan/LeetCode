# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        ret = TreeNode(preorder.pop(0))
        def rec(retpointer, inordl, inordr):
            # print(inordl, inordr)
            if preorder:
                if preorder[0] in inordl:
                    retpointer.left = TreeNode(preorder.pop(0))
                    if inordl:
                        valind = inordl.index(retpointer.left.val)
                        left = inordl[0: valind]
                        right = inordl[valind+1::]
                        rec(retpointer.left, left, right)
            if preorder:
                if preorder[0] in inordr:
                    retpointer.right = TreeNode(preorder.pop(0))
                    if inordr:
                        valind = inordr.index(retpointer.right.val)
                        left = inordr[0: valind]
                        right = inordr[valind+1::]
                        rec(retpointer.right, left, right)

        valind = inorder.index(ret.val)
        left = inorder[0: valind]
        right = inorder[valind+1::]
        rec(ret, left, right)
        # print(ret)
        return ret