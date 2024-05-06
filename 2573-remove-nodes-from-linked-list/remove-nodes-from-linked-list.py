# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ma = [0]
        def reco(nd):
            if nd != None:
                ret = reco(nd.next)
                if nd.val >= ma[0]:
                    ma[0] = nd.val
                    return ListNode(nd.val, ret)
                return ret
            else:
                return None
        return reco(head)