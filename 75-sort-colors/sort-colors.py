class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def rec(li):
            mid = len(li) // 2
            li1 = li[0:mid]
            li2 = li[mid::]
            if len(li1) > 1:
                li1 = rec(li1)
            if len(li2) > 1:
                li2 = rec(li2) 
            temp = []
            while li1 and li2:
                if li1[0] <= li2[0]:
                    temp.append(li1.pop(0))
                else:
                    temp.append(li2.pop(0))
            if li1:
                temp = temp + li1
            if li2:
                temp = temp + li2
            return temp
        nums[:] = rec(nums)[:]