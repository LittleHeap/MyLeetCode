class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:

        m = len(A)
        n = len(A[0])

        done = set()
        done.add((0, 0))
        q = [(-A[0][0], 0, 0)]

        while q:
            val, i, j = heapq.heappop(q)
            if i == m - 1 and j == n - 1:
                return -val
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in done:
                    done.add((x, y))
                    heapq.heappush(q, (-min(A[x][y], -val), x, y))