class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        res = 0

        for i in range(1, len(prices)):
            cur = prices[i] - prices[i - 1]
            if cur > 0:
                res += cur

        return res