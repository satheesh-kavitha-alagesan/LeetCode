# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# #Solution1
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         idvault = {}
#         inc = 0
#         while head:
#             if id(head) in idvault:
#                 return idvault[id(head)]
#             else:
#                 idvault[id(head)] = head
#             head = head.next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if not fast or not fast.next:
            return None

        slow2 = head
        while slow2 != slow:
            slow = slow.next
            slow2 = slow2.next
        return slow