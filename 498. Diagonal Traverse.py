class Solution:
    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:

        if not A:
            return A
        res = []

        m = len(A)
        n = len(A[0])

        total = m * n
        d = 1
        i, j = 0, 0

        while len(res) < total:
            res.append(A[i][j])
            print(i, j)
            if d == 1:
                i -= 1
                j += 1
                if i == -1 and j == n:
                    i = 1
                    j = n - 1
                    d = 0
                elif i == -1:
                    i = 0
                    d = 0
                elif j == n:
                    i += 2
                    j -= 1
                    d = 0
            else:
                i += 1
                j -= 1
                if j == -1 and i == m:
                    j = 1
                    i = m - 1
                    d = 1
                elif j == -1:
                    j = 0
                    d = 1
                elif i == m:
                    j += 2
                    i -= 1
                    d = 1

        return res