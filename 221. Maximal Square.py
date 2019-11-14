class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        hold = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            for i in range(m):
                if matrix[i][j] == '1':
                    hold[i][j] = 1
        for j in range(n):
            for i in range(1, m):
                if matrix[i][j] == '1':
                    hold[i][j] += hold[i - 1][j]

        res = 0
        for i in range(m):
            for j in range(n):
                if hold[i][j] != 0:
                    res = max(res, 1)
                    h = hold[i][j]
                    for r in range(j + 1, n):
                        if r - j + 1 > h:
                            break
                        h = min(h, hold[i][r])
                        if h == r - j + 1:
                            res = max(res, h * (r - j + 1))
        return res