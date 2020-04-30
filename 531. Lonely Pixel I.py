class Solution:
    def findLonelyPixel(self, A: List[List[str]]) -> int:

        m = len(A)
        if m == 0:
            return 0
        n = len(A[0])
        if n == 0:
            return 0

        row = [0 for _ in range(m)]
        col = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if A[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 'B':
                    res += (1 if row[i] == 1 and col[j] == 1 else 0)

        return res