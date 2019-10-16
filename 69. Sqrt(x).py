class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0 or x == 1:
            return x

        l = 1
        r = x
        while l < r:
            mid = (l + r) // 2
            if mid * mid == x or (mid * mid < x and (mid + 1) * (mid + 1) > x):
                return mid
            elif mid * mid > x:
                r = mid
            else:
                l = mid