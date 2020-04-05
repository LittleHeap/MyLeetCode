class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = (l + r) // 2
            d = 1
            cur = 0
            for w in weights:
                if cur + w <= mid:
                    cur += w
                else:
                    cur = w
                    d += 1
            if d <= D:
                r = mid
            else:
                l = mid + 1
        return l