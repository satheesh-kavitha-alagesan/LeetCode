class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)
        maxvol = 0
        while True:
            leng = end - (start +1)
            if start == end - 1:
                break
            elif height[start] > height[end - 1]:
                curvol = height[end - 1] * leng
                end -= 1
            else:
                curvol = height[start] * leng
                start  += 1
            maxvol = max(maxvol, curvol)
        return maxvol