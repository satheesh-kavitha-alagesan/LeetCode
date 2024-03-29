# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        idvault = {}
        inc = 0
        while head:
            if id(head) in idvault:
                return idvault[id(head)]
            else:
                idvault[id(head)] = head
            head = head.next