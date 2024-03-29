# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        st = slow.next
        slow.next = None
        stack = []
        while st:
            stack.append(st.val)
            st = st.next

        while dummy:
            temp = dummy.next
            if stack:
                dummy.next = ListNode(stack.pop())
                dummy.next.next = temp
            dummy = temp
        return head