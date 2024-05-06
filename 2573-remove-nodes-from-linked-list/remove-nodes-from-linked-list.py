# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1
# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         ma = [0]
#         def reco(nd):
#             if nd != None:
#                 ret = reco(nd.next)
#                 if nd.val >= ma[0]:
#                     ma[0] = nd.val
#                     return ListNode(nd.val, ret)
#                 return ret
#             else:
#                 return None
#         return reco(head)

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #first reverse the list
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        curr = prev
        while curr:
            while curr.next and curr.val>curr.next.val:
                curr.next = curr.next.next
            curr=curr.next

        curr = prev
        prev = None
        while curr:
            next = curr.next
            curr.next=prev
            prev =curr
            curr = next
        return prev