class Solution:
    def integerReplacement(self, n: int) -> int:

        res = [float('inf')]

        def deep(num, step):
            if num == 1:
                res[0] = min(res[0], step)
            else:
                if num % 2 == 0:
                    deep(num // 2, step + 1)
                else:
                    deep(num + 1, step + 1)
                    deep(num - 1, step + 1)

        deep(n, 0)

        return res[0]