class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        hold = []

        for ele in points:
            heapq.heappush(hold, ((ele[0] ** 2 + ele[1] ** 2), ele[0], ele[1]))

        res = []

        for _ in range(K):
            cur = heapq.heappop(hold)
            res.append([cur[1], cur[2]])

        return res