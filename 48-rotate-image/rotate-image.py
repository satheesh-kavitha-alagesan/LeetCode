class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for idx, arr in enumerate(zip(*matrix)):
        #     matrix[idx] = arr[::-1]

        for rind in range(len(matrix)):
            for cind in range(len(matrix)):
                if cind < rind:
                    matrix[rind][cind], matrix[cind][rind] = matrix[cind][rind], matrix[rind][cind]
        for rind in range(len(matrix)):
            matrix[rind] = matrix[rind][::-1]