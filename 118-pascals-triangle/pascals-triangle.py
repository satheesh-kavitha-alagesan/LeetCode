class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(1, numRows+1):
            temp = []
            for j in range(0, i):
                if j == 0:
                    temp.append(1)
                    continue
                elif j == (i-1):
                    temp.append(1)
                    continue
                else:
                    temp.append(ret[-1][j-1]+ret[-1][j])
            ret.append(temp)
            temp = []
        return ret