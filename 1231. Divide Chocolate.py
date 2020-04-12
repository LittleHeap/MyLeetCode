class Solution:
    def maximizeSweetness(self, A: List[int], K: int) -> int:

        l, r = min(A), sum(A)
        while l <= r:
            mid = (l + r) // 2
            cur = cuts = 0
            for a in A:
                cur += a
                if cur >= mid:
                    cuts += 1
                    cur = 0
            if cuts - 1 >= K:
                l = mid + 1
            else:
                r = mid - 1
        return r