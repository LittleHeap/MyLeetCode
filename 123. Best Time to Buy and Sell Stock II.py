class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        cur = [-prices[0], 0, -prices[0], 0]
        # buy1 sell1 buy2 sell2

        for i in range(1, len(prices)):
            cur = [max(cur[0], -prices[i]), max(cur[1], prices[i] + cur[0]), max(cur[2], cur[1] - prices[i]),
                   max(cur[3], prices[i] + cur[2])]

        return cur[-1]