class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = 1
        r = x
        while l <= r:
            mid = (l + r) // 2
            m = mid ** 2
            n = (mid + 1) ** 2
            if m <= x and n > x:
                return mid
                break
            elif m > x:
                r = mid - 1
            else:
                l = mid + 1
