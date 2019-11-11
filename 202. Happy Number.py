class Solution:
    def isHappy(self, n: int) -> bool:

        save = set()
        while 1:
            nums = list(str(n))
            res = 0
            for ele in nums:
                res += int(ele) ** 2
            if res == 1:
                return True
            if res not in save:
                save.add(res)
                n = res
            else:
                return False