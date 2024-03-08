class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ##Solution1
        # def rec(li):
        #     mid = len(li) // 2
        #     li1 = li[0:mid]
        #     li2 = li[mid::]
        #     if len(li1) > 1:
        #         li1 = rec(li1)
        #     if len(li2) > 1:
        #         li2 = rec(li2) 
        #     temp = []
        #     while li1 and li2:
        #         if li1[0] <= li2[0]:
        #             temp.append(li1.pop(0))
        #         else:
        #             temp.append(li2.pop(0))
        #     if li1:
        #         temp = temp + li1
        #     if li2:
        #         temp = temp + li2
        #     return temp
        # nums[:] = rec(nums)[:]

        ##Solution2
        # mapping = {0:0, 1:0, 2:0}
        # for num in nums:
        #     mapping[num] += 1
        # nums[:] = [0]*mapping[0] + [1]*mapping[1] + [2]*mapping[2]

        #Solution3
        n = len(nums)
        l, r, i = 0, n-1, 0

        while True:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                i+=1
                l+=1
            elif nums[i] == 1:
                i+=1
            else:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            if i > r:
                break