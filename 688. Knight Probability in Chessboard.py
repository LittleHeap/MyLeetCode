class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:

        d = {}

        def dfs(i, j, p, k):
            if k == 0:
                return p
            else:
                cur = 0
                for x, y in [(i - 2, j - 1), (i - 1, j - 2), (i - 2, j + 1), (i - 1, j + 2), (i + 2, j + 1),
                             (i + 1, j + 2), (i + 2, j - 1), (i + 1, j - 2)]:
                    if x >= 0 and x < N and y >= 0 and y < N:
                        if (x, y, k - 1) not in d:
                            d[(x, y, k - 1)] = dfs(x, y, p / 8, k - 1)
                        cur += d[(x, y, k - 1)]
                return cur

        return dfs(r, c, 1, K)
