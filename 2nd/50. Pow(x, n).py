class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return float(1)

        if n < 0:
            x = 1 / x
            n = -n

        def deep(t):
            if t == 1:
                return x
            if t % 2 == 1:
                return x * deep((t - 1) // 2) ** 2
            else:
                return deep(t // 2) ** 2

        return deep(n)
