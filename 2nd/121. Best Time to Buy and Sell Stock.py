class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        for i in range(len(prices)):
            if i == 0:
                low = prices[i]
            else:
                res = max(prices[i] - low, res)
                low = min(low, prices[i])

        if res < 0:
            return 0
        else:
            return res
