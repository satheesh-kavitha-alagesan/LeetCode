# class Solution:
#     def trap(self, height: List[int]) -> int:
#         mh = max(height)
#         block_vol = sum(height)

#         left = 0
#         max_left = 0
#         while height[left] < mh:
#             if height[left] > max_left:
#                 max_left = height[left]
            
#             height[left] = max_left
#             left += 1
        
#         right = len(height)-1
#         max_right = 0
#         while height[right] < mh:
#             if height[right] > max_right:
#                 max_right = height[right]
            
#             height[right] = max_right
#             right -= 1
        
#         filled_vol = sum(height[0:left]+height[right:]) + (right-left)*mh
#         return filled_vol - block_vol

class Solution:
    def trap(self, height: List[int]) -> int:
        maxh = max(height)
        blockvol = sum(height)

        left = 0
        maxleft = 0

        while height[left] < maxh:
            if height[left] < maxleft:
              height[left] = maxleft
            maxleft = height[left]
            left+=1
        
        right = len(height) -1
        maxright = 0
        while height[right] < maxh:
            if height[right] < maxright:
                height[right] = maxright
            maxright = height[right]
            right -= 1

        totalvol = sum(height[0:left]+height[right:]) + (right-left)*maxh
        return totalvol - blockvol
