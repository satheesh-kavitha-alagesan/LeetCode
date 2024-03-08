# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         previous = head.val
#         flag = True if head.val == head.next.val else False
#         catch = head
#         while head.next:
#             if catch.val != previous:
#                 catch = catch.next

class Solution(object):
    def deleteDuplicates(self, head):
        fake = ListNode(-1)
        fake.next = head
        curr, prev = head, fake
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = prev.next
        return fake.next
