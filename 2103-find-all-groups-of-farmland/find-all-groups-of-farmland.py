class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m,n = len(land), len(land[0])
        ret = []
        temp = [False,False,False,False]
        def rec(row, col):
            if (row < 0 or row >= m) or (col < 0 or col >= n):
                return
            if land[row][col] == 0:
                return
            if (not temp[2]) or (temp[2] < row):
                temp[2] = row
            if (not temp[3]) or (temp[3] < col):
                temp[3] = col
            land[row][col] = 0
            rec(row+1, col)
            rec(row-1, col)
            rec(row, col+1)
            rec(row, col-1)

        for row in range(0,m):
            for col in range(0,n):
                if land[row][col] == 1:
                    temp[0] = row
                    temp[1] = col
                    rec(row, col)
                    ret.append(temp)
                    temp = [False,False,False,False]
        return ret