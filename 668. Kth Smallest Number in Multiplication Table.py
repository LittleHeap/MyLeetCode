class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        if m > n:
            m, n = n, m

        l, r = 1, m * n

        while l < r:
            mid = (l + r) >> 1
            if sum(min(mid // r, n) for r in range(1, m + 1)) < k:
                l = mid + 1
            else:
                r = mid
        return l