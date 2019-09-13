class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0

        t = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i - 1 >= 0:
                        t[i][j] = t[i - 1][j] + 1
                    else:
                        t[i][j] = 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    ans = max(ans, t[i][j])
                    h = t[i][j]
                    for k in range(j + 1, n):
                        h = min(h, t[i][k])
                        if matrix[i][k] == '1':
                            ans = max(ans, h * (k - j + 1))
                        elif matrix[i][k] == '0':
                            ans = max(ans, h * (k - j))
                            break
        return ans
