class Solution:
    def findBlackPixel(self, A: List[List[str]], N: int) -> int:

        m = len(A)
        if m == 0:
            return 0
        n = len(A[0])
        if n == 0:
            return 0

        row = [0 for _ in range(m)]
        col = [0 for _ in range(n)]

        d = defaultdict(int)
        for i in range(m):
            d[''.join(A[i])] += 1
            for j in range(n):
                if A[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 'B' and col[j] == N and row[i] == N:
                    res += (1 if d[''.join(A[i])] == col[j] else 0)

        return res
