class Solution:
    def findDerangement(self, n: int) -> int:

        if n == 1:
            return 0

        mod = 10 ** 9 + 7

        a, b = 0, 1

        for i in range(2, n):
            b, a = (a + b) * i % mod, b

        return b