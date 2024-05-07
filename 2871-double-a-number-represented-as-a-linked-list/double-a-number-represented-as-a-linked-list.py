# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        prev = None

        while cur:
            nx = cur.next
            cur.next = prev
            prev = cur
            cur = nx

        ret = None
        rem = 0
        while prev:
            val = (prev.val * 2) + rem
            ret = ListNode( val % 10, ret )
            if val // 10 > 0:
                rem = val // 10
            else:
                rem = 0
            prev = prev.next
        if rem > 0:
            ret = ListNode( rem, ret )
        return ret