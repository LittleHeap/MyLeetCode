class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        self.res = 0
        self.cur = 0

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        def deep(i, j):
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == 1:
                    grid[x][y] = 0
                    self.cur += 1
                    deep(x, y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.cur = 1
                    grid[i][j] = 0
                    deep(i, j)
                    self.res = max(self.res, self.cur)

        return self.res