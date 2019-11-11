class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        ans = 0

        def deep(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            else:
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    deep(i - 1, j)
                    deep(i + 1, j)
                    deep(i, j + 1)
                    deep(i, j - 1)

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    ans += 1
                    deep(x, y)
        return ans
