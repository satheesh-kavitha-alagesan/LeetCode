# #Soution 1
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         ret = 1
#         while ret*ret <= x:
#             ret +=1
#         return ret -1

#Solution 2
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x

        while l < r:
            mid = l + (r - l + 1) // 2

            if mid ** 2 <= x:
                l = mid
            else:
                r = mid - 1

        return l