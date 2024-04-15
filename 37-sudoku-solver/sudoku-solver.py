# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         traspose = list(zip(*board))
#         reqval = {0,1,2,3,4,5,6,7,8,9}
#         row = { i: set() for i in range(9)}
#         col = { i: set() for i in range(9)}
#         grid = { i: set() for i in range(9)}

#         for rind in range(len(board)):
#             for cind in range(len(board)):
#                 if board[i][j] != '.':
#                     row[rind].update(board[i][j])
#                     col[cind].update(board[i][j])
#                     gridmap = (i//2 * 3) + j
#                     grid[gridmap].update(board[i][j])

#         entry = []
#         for rind in range(len(board)):
#             for cind in range(len(board)):
#                 if board[rind][cind] == '.':
#                     gridmap = (i//2 * 3) + j
#                     board[rind][cind] = reqval - (row[rind] + col[cind] + grid[gridmap])
#                     if len(board[rind][cind]) == 1:
#                         entry.append([rind,cind])
        
#         def fill(rind, cind, board=board):
#             val = list(board[rind][cind])[0]
#             board[rind][cind] = val
#             if val in row[rind]:
#                 row[rind].remove(val)
#                 for _r in range(board[])
#             if val in col[cind]:
#                 col[cind].remove(val)
#             gridmap = (rind//2 * 3) + cind
#             if val in grid[gridmap]:
#                 grid[gridmap].remove(val)
            
# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         n = 9
#         def isValid(row, col, ch):
#             row, col = int(row), int(col)
#             for i in range(9):
#                 if board[i][col] == ch:
#                     return False
#                 if board[row][i] == ch:
#                     return False
                
#                 if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
#                     return False
#             return True  
#         def solve(row, col):
#             if row == n:
#                 return True
#             if col == n:
#                 return solve(row+1, 0)
            
#             if board[row][col] == ".":
#                 for i in range(1, 10):
#                     if isValid(row, col, str(i)):
#                         board[row][col] = str(i)
                        
#                         if solve(row, col + 1):
#                             return True
#                         else:
#                             board[row][col] = "."
#                 return False
#             else:
#                 return solve(row, col + 1)
#         solve(0, 0)
		

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        def isValid(nrow, ncol, ch):
            nrow, ncol = int(nrow), int(ncol)
            for num in range(9):
                if board[num][ncol] == ch:
                    return False
                if board[nrow][num] == ch:
                    return False
                if board[3*(nrow//3)+(num//3)][3*(ncol//3)+(num%3)] == ch:
                    return False
            return True
        
        def solve(row, col):
            if row == n:
                return True
            if col == n:
                return solve(row+1, 0)
            if board[row][col] == '.':
                for i in range(1,10):
                    if isValid(row, col, str(i)):
                        board[row][col] = str(i)
                        if solve(row, col+1):
                            return True
                        else:
                            board[row][col] = '.'
                return False
            else:
                return solve(row, col+1)
        solve(0,0)
        return board