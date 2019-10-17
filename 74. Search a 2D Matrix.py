class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        s = None
        for i in range(m):
            if matrix[i][0] <= target:
                s = i

        if s is None:
            return False
        else:
            for j in range(n):
                if matrix[s][j] == target:
                    return True
            return False