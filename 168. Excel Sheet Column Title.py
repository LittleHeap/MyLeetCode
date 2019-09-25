class Solution:
    def convertToTitle(self, n: int) -> str:

        s = {}

        for i in range(65, 91):
            s[i - 64] = chr(i)

        p = 0
        hold = 26
        while hold < n:
            p += 1
            hold += 26 * (26 ** p)

        res = []
        while n != 0:
            cur = n // (26 ** p)
            n -= cur * (26 ** p)
            if n == 0 and p != 0:
                n += cur * (26 ** p)
                cur -= 1
                n -= cur * (26 ** p)
            res.append(s[cur])
            p -= 1

        return ''.join(res)
