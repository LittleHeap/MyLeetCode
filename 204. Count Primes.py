import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        ans = 0
        ans += 1
        no = set()
        no.add(2)
        i = 1
        while 2 * i < n:
            no.add(2 * i)
            i += 1
        for i in range(3, n, 2):
            if i in no:
                continue
            r = 1
            while i * r < n:
                no.add(i * r)
                r += 1
            ans += 1
            for j in range(3, int(math.sqrt(i)) + 1, 2):
                if i % j == 0:
                    ans -= 1
                    break

        return ans
