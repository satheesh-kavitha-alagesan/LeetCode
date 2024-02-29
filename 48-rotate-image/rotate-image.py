class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for idx, arr in enumerate(zip(*matrix)):
            matrix[idx] = arr[::-1]