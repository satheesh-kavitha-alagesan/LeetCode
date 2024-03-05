class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dp = [[0]*n for _ in range(n)]
        startind = [0,0]
        count = 1
        cur = 'l_to_r'
        row, col = (0,0)
        while count <= n*n:
            print(row,col)
            dp[row][col] = count
            count +=1
            if cur == 'l_to_r':
                if col +1 < len(dp[col]):
                    if dp[row][col +1] == 0:
                        col = col+1
                        continue
                cur = 't_to_b'
                row = row+1
            elif cur == 't_to_b':
                if row +1 < len(dp):
                    if dp[row+1][col] == 0:
                        row = row+1
                        continue
                cur = 'r_to_l'
                col = col -1
            elif cur == 'r_to_l':
                if col -1 >= 0:
                    if dp[row][col -1] ==0:
                        col = col-1
                        continue
                cur = 'b_to_t'
                row = row -1
            elif cur == 'b_to_t':
                if row -1 >=0:
                    if dp[row -1][col] == 0:
                        row = row -1
                        continue
                cur = 'l_to_r'
                col = col +1

        print(dp)
        return dp