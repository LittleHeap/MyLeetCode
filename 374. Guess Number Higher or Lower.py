# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        l = 1
        r = n
        mid = (r + l) // 2
        while guess(mid) != 0:
            print(mid)
            if guess(mid) == -1:
                r = mid - 1
            else:
                l = mid + 1
            mid = (r + l) // 2

        return mid