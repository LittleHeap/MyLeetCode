class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        l, r = 0, int(math.sqrt(c) + 1)

        while l <= r:
            # print(l ,r)
            cur = l ** 2 + r ** 2
            if cur == c:
                return True
            elif cur > c:
                r -= 1
            else:
                l += 1

        return False