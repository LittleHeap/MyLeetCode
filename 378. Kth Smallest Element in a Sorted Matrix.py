class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        res = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(res, matrix[i][j])

        while k > 1:
            heapq.heappop(res)
            k -= 1

        return heapq.heappop(res)