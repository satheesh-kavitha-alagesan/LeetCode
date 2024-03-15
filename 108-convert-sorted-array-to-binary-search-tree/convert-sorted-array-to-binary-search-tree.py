# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         split = len(nums) // 2
#         if len(nums) % 2==1:
#             l1 = nums[0:split+1]
#             l2 = nums[split+1::]
#         else:
#             l1 = nums[0:split]
#             l2 = nums[split::]
#         print(l1)
#         print(l2)
#         li1 = TreeNode(l1.pop(0))
#         for i in l1:
#             li1 = TreeNode(val = i, left = li1)
#         li2 = TreeNode(l2.pop(0))
#         for i in l2:
#             li2 = TreeNode(val = i, left = li2)
#         li1.right = li2

#         return li1

# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         if len(nums) == 0:
#             return None
#         mid = len(nums)//2
#         root = TreeNode(nums[mid])
#         root.left = self.sortedArrayToBST(nums[:mid])
#         root.right = self.sortedArrayToBST(nums[mid+1:])
#         return root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l: int, r: int):
            if l > r:
                return None
            else:
                m = (l + r) // 2
                print(nums[m])
                root = TreeNode(nums[m])
                root.left = helper(l, m - 1)
                root.right = helper(m + 1, r)
                return root
        
        return helper(0, len(nums) - 1)
