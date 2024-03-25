# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         flagList = []
#         index = []
#         def end(r, c):
#             index.append((r,c))
#             rowaddFl, coladdFl, rowsubFl, colsubFl = False, False, False, False
#             row, col = r, c
#             while 0 <= row >= len(board):
#                 if board[row][col] == 'X':
#                     rowaddFl = True
#                     break
#                 row+=1
#             row, col = r, c
#             while 0 <= col >= len(board):
#                 if board[row][col] == 'X':
#                     coladdFl = True
#                     break
#                 col+=1
#             row, col = r, c
#             while 0 <= row >= len(board):
#                 if board[row][col] == 'X':
#                     rowsubFl = True
#                     break
#                 row-=1
#             row, col = r, c
#             while 0 <= col >= len(board):
#                 if board[row][col] == 'X':
#                     colsubFl = True
#                     break
#                 col-=1
#             row, col = r, c
#             board[row][col] = 1
#             print(f'{row = }, {col = }')
#             print(f'{rowaddFl = }, {rowaddFl = }, {rowaddFl = }, {rowaddFl = }')
#             flagList.append(rowaddFl and coladdFl and rowsubFl and colsubFl)
#             if 0 <= row +1 > len(board):
#                 if board[row+1][col] == 'O':
#                     end(row+1, col)
#             if 0 <= row-1 > len(board):
#                 if board[row-1][col] == 'O':
#                     end(row-1, col)
#             if 0 <= col +1 > len(board):
#                 if board[row][col+1] == 'O':
#                     end(row, col+1)
#             if 0 <= col-1 > len(board):
#                 if board[row][col-1] == 'O':
#                     end(row, col-1)
#         for rowind in range(len(board)):
#             for colind in range(len(board[0])):
#                 if board[rowind][colind] == 'O':
#                     end(rowind,colind)
#                     if all(flagList):
#                         for r,c in index:
#                             board[r][c] == 'X'
#                     else:
#                         index = []
#                         flagList = []
#         print(board)
#         return board

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i,j,mark):
            nonlocal board
            if( (i < 0) or (j < 0 ) or (i >= m) or (j >= n) ):
                return False;
            elif(board[i][j] == 'X' or board[i][j] == mark):
                return True
            else:
                res = True
                board[i][j] = mark
                for d in direc:
                    x = i+d[0]
                    y = j+d[1]
                    res = dfs(x,y,mark) and res; 
                return res
        
        direc = [[-1,0],[0,-1],[1,0],[0,1]]
        m , n = len(board), len(board[0]);
        
        for i in range(0,m):
            for j in range(0,n):
                if( board[i][j] == "O" ):
                    if( dfs(i , j,'1') ): 
                        dfs(i,j,"X") 
        for i in range(0,m):
            for j in range(0,n):
                if(board[i][j] == '1'): board[i][j] = "O"