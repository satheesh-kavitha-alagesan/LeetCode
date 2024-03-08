class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        while len(matrix) > 1:
            mid = len(matrix) // 2
            # print(matrix)
            # print(mid)
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                if target in matrix[mid]:
                    return True
                else:
                    return False
            elif target < matrix[mid][-1]:
                matrix = matrix[0:mid]
            else:
                matrix = matrix[mid::]
        if target in matrix[0]:
            return True
        return False