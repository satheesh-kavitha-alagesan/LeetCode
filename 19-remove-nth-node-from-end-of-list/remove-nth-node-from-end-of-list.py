# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        class RemoveNode:
            def __init__(self):
                self.ret = ListNode()
                self.cou = 0
                self.end  = False

            def rec(self, head):
                if head.next:
                    self.rec(head.next)
                else:
                    self.end = True
                if self.end == True:
                    self.cou +=1
                    if self.cou != n:
                        self.ret.val = head.val
                        self.ret = ListNode(val = 0, next = self.ret)
        res= RemoveNode()
        res.rec(head)
        res = res.ret
        return res.next