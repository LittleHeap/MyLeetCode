class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        if not sticks:
            return 0

        res = 0

        hold = []
        for ele in sticks:
            heapq.heappush(hold, ele)

        while len(hold) > 1:
            cost = heapq.heappop(hold) + heapq.heappop(hold)
            res += cost
            heapq.heappush(hold, cost)

        return res