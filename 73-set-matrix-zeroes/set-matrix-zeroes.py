# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         changed = set()
#         for r in range(len(matrix)):
#             for c in range(len(matrix[0])):
#                 if matrix[r][c] == 0 and (r,c) not in changed:
#                     self.change(matrix, r,c, changed) 

            
#     def change(self, matrix, r, c, changed):
        
#         for cr in range(0, len(matrix)):
#             if matrix[cr][c] != 0:
#                 matrix[cr][c] = 0
#                 changed.add((cr,c))

#         for cc in range(0, len(matrix[0])):
#             if matrix[r][cc] != 0:
#                 matrix[r][cc] = 0
#                 changed.add((r,cc))

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=len(matrix)
        cols=len(matrix[0])
        temp=[]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    temp.append((i,j))
        for p,q in temp:
            matrix[p]=[0]*cols
            for r in range(rows):
                matrix[r][q]=0            

        