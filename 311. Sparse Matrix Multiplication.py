class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        ma = len(A)
        na = len(A[0])

        mb = len(B)
        nb = len(B[0])

        res = [[0 for _ in range(nb)] for _ in range(ma)]

        for i in range(ma):
            for j in range(nb):
                cur = 0
                for x in range(na):
                    cur += A[i][x] * B[x][j]
                res[i][j] = cur

        return res