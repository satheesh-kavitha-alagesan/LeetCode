# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# #Solution has issue Correct them
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if (head == None) or (head.next == None):
#             return head
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         slow.next = None

#         left = self.sortList(slow)
#         right = self.sortList(fast)
#         print(f'{left = }')
#         print(f'{right = }')

#         ret= dummy = ListNode()
#         while left and right:
#             if left.val < right.val:
#                 dummy.next = ListNode(left.val)
#                 dummy= dummy.next
#                 left = left.next
#             else:
#                 dummy.next = ListNode(right.val)
#                 dummy= dummy.next
#                 right = right.next
#         if left:
#             dummy.next = left
#         if right:
#             dummy.next = right
#         return ret.next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right

        return dummy.next