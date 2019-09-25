class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        m = bin(m)
        n = bin(n)

        if len(m) != len(n):
            return 0

        l = 0
        length = len(m)
        while l < length and m[l] == n[l]:
            l += 1

        l -= 2
        m = list(m)[2:]
        for i in range(len(m) - 1, l - 1, -1):
            m[i] = '0'

        m = ''.join(m)

        return (int(m, 2))
