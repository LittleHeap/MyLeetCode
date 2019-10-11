class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return float(1)

        if n < 0:
            n = -n
            x = 1 / x

        def deep(cur):
            if cur == 1:
                return x
            else:
                p = deep(cur // 2)
                if cur % 2 == 1:
                    return p * p * x
                else:
                    return p * p

        res = deep(n)
        return float(res)