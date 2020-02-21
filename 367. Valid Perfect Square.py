class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return 1
        l = 1
        r = num
        mid = (l + r - 1) // 2

        while l < r:
            res = mid ** 2
            if res == num or l ** 2 == num or r ** 2 == num:
                return 1
            else:
                if res > num:
                    r = mid - 1
                else:
                    l = mid + 1
                mid = (l + r - 1) // 2

        return 0