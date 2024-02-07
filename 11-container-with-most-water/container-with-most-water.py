# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         start = 0
#         end = len(height)
#         maxvol = 0
#         while True:
#             leng = end - (start +1)
#             if start == end - 1:
#                 break
#             elif height[start] > height[end - 1]:
#                 curvol = height[end - 1] * leng
#                 end -= 1
#             else:
#                 curvol = height[start] * leng
#                 start  += 1
#             maxvol = max(maxvol, curvol)
#         return maxvol

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea