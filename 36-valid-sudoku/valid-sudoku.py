# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         def check(rec):
#             occur = {}
#             for r in rec:
#                 if r in occur.keys():
#                     occur[r]+=1
#                 else:
#                     occur[r]=1
#             for _key, _value in occur.items():
#                 if (_key != '.') and (_value > 1):
#                     return False
#             return True

#         for row in board:
#             if not check(row):
#                 return False
        
#         for row in list(zip(*board)):
#             if not check(row):
#                 return False
        
#         for rownum in list(range(0,9, 3)):
#             transform = list(zip(*board[rownum : rownum+3]))
#             for colnum in list(range(0,9, 3)):
#                 if not check([item for row in transform[colnum: colnum+3] for item in row]):
#                     return False
#         return True

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         seen = set()

#         for i in range(9):
#             for j in range(9):
#                 num = board[i][j]
#                 if num != '.':
#                     row_key = (i, num)
#                     col_key = (num, j)
#                     box_key = (i // 3, j // 3, num)
                    
#                     if (row_key in seen) or (col_key in seen) or (box_key in seen):
#                         return False

#                     seen.update([row_key, col_key, box_key])

#         return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val.isalnum():
                    k = i//3 * 3 + j//3
                    if val in row[i] or val in col[j] or val in grid[k]:
                        return False
                    else:
                        row[i].add(val)
                        col[j].add(val)
                        grid[k].add(val)

        return True