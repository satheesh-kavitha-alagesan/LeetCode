# class Solution:
#     def minFallingPathSum(self, grid: List[List[int]]) -> int:
#         def rec(gr, ignore):
#             print(f'{gr = }, {ignore = }')
#             curli = gr.pop(0)
#             mini = float('inf')
#             nignore = 0
#             for ind, m in enumerate(curli):
#                 if m < mini and ind != ignore:
#                     print(f'{m = }')
#                     mini = m
#                     nignore = ind
#             if gr:
#                 return mini + rec(gr, nignore)
#             else:
#                 return mini
#         return rec(grid, None)

class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        DP = grid[0]

        for i in range(1, N):
            indx1 = DP.index(min(DP))
            indx2 = DP.index(min(DP[:indx1] + DP[indx1+1:]))
            for j in range(N):
                if j != indx1:
                    grid[i][j] += DP[indx1]
                else:
                    grid[i][j] += DP[indx2]
            DP = grid[i]

        return min(DP)