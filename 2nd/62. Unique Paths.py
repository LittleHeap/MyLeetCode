class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 0 or m == 0:
            return 0

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(m):
            dp[0][i] = 1

        for j in range(n):
            dp[j][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return (dp[-1][-1])
