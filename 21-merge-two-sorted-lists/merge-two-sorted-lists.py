# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def rec(l1, l2):
            if l1 and l2:
                temp=ListNode()
                if l1.val <= l2.val:
                    temp.val = l1.val
                    l1 = l1.next
                else:
                    temp.val = l2.val
                    l2 = l2.next
                temp.next = rec(l1, l2)
                return temp
            elif l1:
                return l1
            else:
                return l2
        return rec(list1, list2)