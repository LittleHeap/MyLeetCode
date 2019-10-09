class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend * divisor < 0:
            flag = 1
        else:
            flag = 0

        dividend = abs(dividend)
        divisor = abs(divisor)

        res = dividend // divisor
        if flag:
            res = -res

        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31
        else:
            return res
