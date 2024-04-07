# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prevEnd = ListNode(next=head)
        curr = currEnd = head
        prev = None
        cnt = 1
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
            if cnt%k==0:
                prevEnd.next,prevEnd,currEnd,prev = prev,currEnd,curr,None
            cnt += 1

        curr = prev
        prev = None
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
        prevEnd.next = prev

        return dummy.next