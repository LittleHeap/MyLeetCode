class Solution:
    def canIWin(self, max: int, target: int) -> bool:

        if (1 + max) * max // 2 < target:
            return False

        d = {}

        def deep(opt, remain):
            if opt in d:
                return d[opt]
            if opt[-1] >= remain:
                return True
            for i, num in enumerate(opt):
                if not deep(opt[:i] + opt[i + 1:], remain - num):
                    d[opt] = True
                    return True
            d[opt] = False
            return False

        return deep(tuple([i for i in range(1, max + 1)]), target)