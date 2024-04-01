class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                li.append(nums1.pop(0))
            else:
                li.append(nums2.pop(0))
        if nums1:
            li = li + nums1
        if nums2:
            li = li+ nums2
        if len(li) % 2 == 1:
            return li[len(li) // 2]
        else:
            return (li[(len(li) // 2) -1] + li[(len(li) // 2)]) /2