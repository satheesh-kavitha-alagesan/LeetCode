# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = ListNode(-1)
        lc = l
        r = ListNode(-1)
        rc = r
        while head:
            if head.val < x:
                lc.next = head
                lc = lc.next
            else:
                rc.next = head
                rc = rc.next
            head = head.next
        rc.next = None
        lc.next = r.next
        return l.next