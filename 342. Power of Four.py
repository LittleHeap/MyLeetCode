class Solution:
    def isPowerOfFour(self, num: int) -> bool:

        while 1:
            if num == 1:
                return 1
            num = num / 4
            if num < 1:
                return 0
