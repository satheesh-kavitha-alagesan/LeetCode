class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        rot = [(0,1), (1, -1), (-1, 1), (1,0)]
        while matrix:
            pop = rot.pop(0)
            row, col = pop
            rot.append(pop)
            if col == 1:
                ret = ret+matrix[row] if row == 0 else ret+list(reversed(matrix[row]))
                del matrix[row]
            elif row == 1:
                temp = []
                ap= []
                for r in matrix:
                    ap.append(r.pop(col))
                    if r:
                        temp.append(r)
                ap = ap if col == -1 else reversed(ap)
                ret += ap
                matrix = temp
        return ret