class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(rec):
            occur = {}
            for r in rec:
                if r in occur.keys():
                    occur[r]+=1
                else:
                    occur[r]=1
            for _key, _value in occur.items():
                if (_key != '.') and (_value > 1):
                    return False
            return True

        for row in board:
            if not check(row):
                return False
        
        for row in list(zip(*board)):
            if not check(row):
                return False
        
        for rownum in list(range(0,9, 3)):
            transform = list(zip(*board[rownum : rownum+3]))
            for colnum in list(range(0,9, 3)):
                if not check([item for row in transform[colnum: colnum+3] for item in row]):
                    return False
        return True