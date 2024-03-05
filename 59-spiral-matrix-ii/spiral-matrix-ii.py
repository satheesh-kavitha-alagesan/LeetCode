# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         dp = [[0]*n for _ in range(n)]
#         startind = [0,0]
#         count = 1
#         cur = 'l_to_r'
#         row, col = (0,0)
#         while count <= n*n:
#             dp[row][col] = count
#             count +=1
#             if cur == 'l_to_r':
#                 if col +1 < len(dp[col]):
#                     if dp[row][col +1] == 0:
#                         col = col+1
#                         continue
#                 cur = 't_to_b'
#                 row = row+1
#             elif cur == 't_to_b':
#                 if row +1 < len(dp):
#                     if dp[row+1][col] == 0:
#                         row = row+1
#                         continue
#                 cur = 'r_to_l'
#                 col = col -1
#             elif cur == 'r_to_l':
#                 if col -1 >= 0:
#                     if dp[row][col -1] ==0:
#                         col = col-1
#                         continue
#                 cur = 'b_to_t'
#                 row = row -1
#             elif cur == 'b_to_t':
#                 if row -1 >=0:
#                     if dp[row -1][col] == 0:
#                         row = row -1
#                         continue
#                 cur = 'l_to_r'
#                 col = col +1
#         return dp

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n - 1
        left = 0
        right = n - 1

        index = 1
        while index <= n*n:
            for x in range(left, right + 1):
                matrix[top][x] = index
                index += 1
            top += 1
            
            for x in range(top, bottom + 1):
                matrix[x][right] = index
                index += 1
            right -= 1

            if top <= bottom:
                for x in range(right, left - 1, -1):
                    matrix[bottom][x] = index
                    index += 1
                bottom -= 1
            
            if left <= right:
                for x in range(bottom, top - 1, -1):
                    matrix[x][left] = index
                    index += 1
                left += 1

        return matrix