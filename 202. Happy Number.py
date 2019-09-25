class Solution:
    def isHappy(self, n: int) -> bool:

        s = set()
        s.add(n)
        while 1:
            cur = list(str(n))
            res = 0
            for ele in cur:
                res += int(ele) ** 2
            if res == 1:
                return True
            if res in s:
                return False
            else:
                s.add(res)
            n = res