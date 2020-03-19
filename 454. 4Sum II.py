class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        d1 = {}
        d2 = {}

        n = len(A)

        for i in range(n):
            for j in range(n):
                d1[A[i] + B[j]] = d1.get(A[i] + B[j], 0) + 1

        for i in range(n):
            for j in range(n):
                d2[C[i] + D[j]] = d2.get(C[i] + D[j], 0) + 1

        res = 0
        for ele in d1:
            if -ele in d2:
                res += d1[ele] * d2[-ele]

        return res