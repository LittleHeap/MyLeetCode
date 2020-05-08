class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:

        if N == 0:
            return 0

        A = [[0 for _ in range(n)] for _ in range(m)]

        A[i][j] = 1
        q = {(i, j): 1}

        while N > 1:
            newq = defaultdict(int)
            N -= 1
            for (i, j) in q:
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x >= 0 and x < m and y >= 0 and y < n:
                        A[x][y] += q[(i, j)]
                        newq[(x, y)] += q[(i, j)]
            q = newq

        res = 0
        t = 10 ** 9 + 7
        for j in range(n):
            res += A[0][j]
            res += A[-1][j]
            res %= t
        for i in range(m):
            res += A[i][0]
            res += A[i][-1]
            res %= t

        return res