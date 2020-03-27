class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:

        d = float('inf')
        res = 0

        A.sort()

        l, r = 0, len(A) - 1

        while l < r:
            if A[l] + A[r] >= K:
                r -= 1
            else:
                temp = K - A[l] - A[r]
                if temp < d:
                    d = temp
                    res = A[l] + A[r]
                l += 1

        if d == float('inf'):
            return -1

        return res