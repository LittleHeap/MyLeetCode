class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:

        if not A:
            return 0

        s = sum(A)
        cur = [i * A[i] for i in range(len(A))]

        t = sum(cur)
        res = t
        for i in range(len(A) - 1, 0, - 1):
            newt = t + s - A[i] * len(A)
            res = max(res, newt)
            t = newt

        return res