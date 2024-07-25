from collections import deque

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def split(li):
            if len(li) > 1:
                mid = len(li) // 2
                return self.sortArray(li[:mid]), self.sortArray(li[mid::])
            else:
                return li, []
        l1, l2 = split(nums)
        l1, l2 = deque(l1), deque(l2)
        ret = []
        while l1 and l2:
            if l1[0] > l2[0]:
                ret.append(l2.popleft())
            else:
                ret.append(l1.popleft())
        if l1:
            ret.extend(l1)
        if l2:
            ret.extend(l2)
        return ret