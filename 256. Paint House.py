class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)
        dp = [[] for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[i] = costs[i]
            else:
                dp[i].append(min(costs[i][0] + dp[i - 1][1], costs[i][0] + dp[i - 1][2]))
                dp[i].append(min(costs[i][1] + dp[i - 1][0], costs[i][1] + dp[i - 1][2]))
                dp[i].append(min(costs[i][2] + dp[i - 1][1], costs[i][2] + dp[i - 1][0]))
        return min(dp[-1])