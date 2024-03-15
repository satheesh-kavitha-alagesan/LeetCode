# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        ans = []
        hashT = defaultdict(list)
        temp = []
        def levelOrd(root, level):
            if root is None:
                return
          
            hashT[level].append(root.val)
        
            levelOrd(root.left, level+1)
            levelOrd(root.right, level+1)
        
        levelOrd(root, 0)
        #print(hashT)
        for i in range(len(hashT)-1,-1,-1):
            ans.append(hashT[i])
            
        return ans

...