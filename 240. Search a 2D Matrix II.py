class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        done = set()
        find = [0]
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        def deep(i, j):
            if find[0] == 1 or (i, j) in done:
                return
            if matrix[i][j] == target:
                find[0] = 1
                return
            else:
                done.add((i, j))
                if i + 1 < m and matrix[i + 1][j] <= target:
                    deep(i + 1, j)
                if j + 1 < n and matrix[i][j + 1] <= target:
                    deep(i, j + 1)


        deep(0, 0)
        return find[0] == 1