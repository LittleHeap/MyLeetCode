class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        save = {}

        temp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if j == 0:
                    temp[i][j] = matrix[i][j]
                else:
                    temp[i][j] = matrix[i][j] + temp[i][j - 1]

        res = 0
        for j1 in range(n):
            for j2 in range(j1, n):
                d = {}
                cur = 0
                d[0] = 1
                for i in range(m):
                    cur += temp[i][j2] - (temp[i][j1 - 1] if j1 > 0 else 0)
                    d[cur] = d.get(cur, 0) + 1
                    res += d.get(cur - target, 0)
                    if target == 0:
                        res -= 1

        return res