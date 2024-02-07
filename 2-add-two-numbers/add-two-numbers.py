# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1Order = ''
        # current = l1
        # while True:
        #     l1Order+= str(current.val)
        #     if not current.next:
        #         break
        #     current = current.next
        # l2Order = ''
        # current = l2
        # while True:
        #     l2Order+= str(current.val)
        #     if not current.next:
        #         break
        #     current = current.next
        # add = int(l1Order) + int(l2Order)
        
        # nval = None
        # for _c in str(add):
        #     retLL =  ListNode(int(_c), nval)
        #     nval = retLL

        # return nval

        # currentl1 = l1
        # currentl2 = l2
        # remainder = 0
        # prev = None
        # v1Stop = False
        # v2Stop = False
        # retLi = []
        # srart = None
        # while True:
        #     if currentl1:
        #         v1 = currentl1.val
        #         currentl1 = currentl1.next
        #     else:
        #         currentl1 = None
        #         v1Stop = True
        #         v1 =0
        #     if currentl2:
        #         v2 = currentl2.val
        #         currentl2 = currentl2.next
        #     else:
        #         currentl2 = None
        #         v2Stop = True
        #         v2 = 0
        #     if v1Stop and v2Stop:
        #         break        
        #     total = v1+v2+remainder
        #     print(v1,v2,remainder, total)
        #     if len(str(total)) > 1:
        #         retLi.append(int(str(total)[-1]))
        #         remainder = int(str(total)[:-1])
        #     else:
        #         retLi.append(total)
        #         remainder = 0
        # if remainder != 0:
        #     retLi.append(remainder)
        # for _c in reversed(retLi):
        #     srart = ListNode(_c, srart)
        # return srart

        dummyHead = ListNode()
        tail = dummyHead
        carry = 0
        while ((l1 is not None) or (l2 is not None) or (carry !=0)):
            curl1val = l1.val if l1 is not None else 0
            curl2val = l2.val if l2 is not None else 0

            add = curl1val + curl2val + carry

            carry = add // 10
            digit = add % 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummyHead.next