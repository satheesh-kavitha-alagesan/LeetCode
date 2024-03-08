## Solution 1 False
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#             global flag
#             flag = False
#             m= len(board)
#             n= len(board[0])
#             def rec(ind, word):
#                 global flag
#                 r, c = ind
#                 if (word == '') or (flag == True):
#                     flag = True
#                     return
#                 elif board[r][c] == word[0]:
#                     if c+1<n:
#                         rec((r,c+1), word[1::])
#                     if c-1 >=0:
#                         rec((r,c-1), word[1::])
#                     if r+1<m:
#                         rec((r+1,c), word[1::])
#                     if r-1 >=0:
#                         rec((r-1,c), word[1::])
#                 else:
#                     return
#             for i in range(m):
#                     for j in range(n):
#                             if not flag:
#                                     rec((i,j), word)
#                             else:
#                                 return True
#             return False

# #Solution2
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         boardDic = defaultdict(int)
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 boardDic[board[i][j]] += 1

#         wordDic = Counter(word)
#         for c in wordDic:
#             if c not in boardDic or boardDic[c] < wordDic[c]:
#                 return False

#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     if self.dfs(i, j, 0, board, word):
#                         return True

#         return False

#     def dfs(self, i, j, k, board, word):
#         if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or \
#         k >= len(word) or word[k] != board[i][j]:
#             return False

#         if k == len(word) - 1:
#             return True

#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#         for x, y in directions:
#             tmp = board[i][j]
#             board[i][j] = -1

#             if self.dfs(i + x, j + y, k + 1, board, word): 
#                 return True

#             board[i][j] = tmp

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
            global flag
            flag = False
            m= len(board)
            n= len(board[0])
            def rec(ind, word, bd):
                global flag
                r, c = ind
                if (word == '') or (flag == True):
                    flag = True
                    return
                elif bd[r][c] == word[0]:
                    tmp = bd[r][c]
                    bd[r][c] = -1
                    if c+1<n:
                        rec((r,c+1), word[1::], bd)
                    if c-1 >=0:
                        rec((r,c-1), word[1::], bd)
                    if r+1<m:
                        rec((r+1,c), word[1::], bd)
                    if r-1 >=0:
                        rec((r-1,c), word[1::], bd)
                    if word[1::] == '':
                        flag = True
                        return
                    bd[r][c] = tmp
                else:
                    return
            for i in range(m):
                    for j in range(n):
                            if not flag:
                                    rec((i,j), word, board)
                            else:
                                return True
            return flag