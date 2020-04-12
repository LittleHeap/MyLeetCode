class Solution:
    def maxSumSubmatrix(self, A: List[List[int]], tar: int) -> int:

        m = len(A)
        n = len(A[0])

        for i in range(m):
            for j in range(1, n):
                A[i][j] += A[i][j - 1]
        # print(A)
        res = float('-inf')
        for l in range(n):
            for r in range(l, n):
                d = [0]
                cur = 0
                for k in range(m):
                    cur += A[k][r] - (A[k][l - 1] if l >= 1 else 0)
                    index = bisect.bisect_left(d, cur - tar)
                    # print(index)
                    if index == len(d):
                        pass
                    elif d[index] == cur - tar:
                        return tar
                    else:
                        res = max(res, cur - d[index])
                    bisect.insort(d, cur)
                    # print(d)

        return res
