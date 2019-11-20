class Solution:
    def numWays(self, n: int, k: int) -> int:

        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k

        dp = [[0, 0] for _ in range(n)]
        dp[1] = [k, k * (k - 1)]

        for i in range(2, n):
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = sum(dp[i - 1]) * (k - 1)

        return sum(dp[-1])