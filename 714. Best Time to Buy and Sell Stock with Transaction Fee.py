class Solution:
    def maxProfit(self, p: List[int], fee: int) -> int:

        dp = [[0, 0] for _ in range(len(p))]
        dp[0][0] = float('-inf')

        for i in range(len(p)):
            if i == 0:
                dp[i][0] = -p[i]
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - p[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + p[i] - fee)

        return dp[-1][1]