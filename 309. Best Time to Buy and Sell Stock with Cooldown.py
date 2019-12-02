class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[float('-inf'), float('-inf'), [float('-inf'), float('-inf')]] for _ in range(n)]

        dp[0][0] = -prices[0]
        dp[0][2][1] = 0

        for i in range(1, n):
            dp[i][0] = dp[i - 1][2][1] - prices[i]
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][2][0] + prices[i])
            dp[i][2][0] = max(dp[i - 1][0], dp[i - 1][2][0])
            dp[i][2][1] = max(dp[i - 1][1], dp[i - 1][2][1])

        return max(dp[-1][1], dp[-1][2][1])