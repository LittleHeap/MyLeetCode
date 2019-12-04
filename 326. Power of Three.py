class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n == 1:
            return 1

        num = 3
        p = 1

        while num <= n:
            if num == n:
                return 1
            else:
                num *= 3
                p += 1

        return 0