class Solution:
    def smallestFactorization(self, a: int) -> int:

        if a == 1:
            return a

        res = ''
        for i in range(9, 1, -1):
            while a > 1 and a % i == 0:
                res = str(i) + res
                a /= i

        return (int(res) if a == 1 and int(res) < 2 ** 31 else 0)