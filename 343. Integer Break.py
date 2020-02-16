class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n)]

        dp[0] = n - 1

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                dp[i] = max(dp[i], dp[j] // (n - j - 1) * (i - j) * (n - j - 1 - i + j))
            dp[i] = max(dp[i], (n - i - 1) * (i + 1))

        return max(dp)