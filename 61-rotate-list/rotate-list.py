# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         count = 1
#         curhead = head
#         end = False
#         rotlen = 0
#         last = l = ListNode()
#         def rec(curhead, end = end, count = count, last = last):
#             print(curhead)
#             if not curhead.next:
#                 print('if')
#                 end = True
#                 rotlen = count//k
#             if end:
#                 print('else')
#                 if rotlen >= 0:
#                     last = ListNode(val = curhead.val, next = last)
#                     rotlen -= 1
#                 else:
#                     l.next = ListNode(val = curhead.val)
#                     l = l.next
#                 return
#             curhead = curhead.next
#             count +=1
#             rec(curhead)

#         rec(curhead)
#         print(last)

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        cur = head
        count = 1
        while cur.next is not None:
            cur = cur.next
            count +=1
        
        cur.next = head

        i = count - (k % count)
        while i > 1:
            head = head.next
            i -=1
        cur = head.next
        head.next = None
        return cur