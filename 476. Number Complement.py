class Solution:
    def findComplement(self, num: int) -> int:
        mi = 0

        while 2 ** mi - 1 < num:
            mi += 1

        return (2 ** mi - 1) ^ num