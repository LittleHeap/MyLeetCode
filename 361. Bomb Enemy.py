class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])

        boom = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    cur = 0
                    for x in range(i - 1, -1, -1):
                        if grid[x][j] == 'W':
                            break
                        if grid[x][j] == 'E':
                            cur += 1
                    for x in range(i + 1, m):
                        if grid[x][j] == 'W':
                            break
                        if grid[x][j] == 'E':
                            cur += 1
                    for y in range(j - 1, -1, -1):
                        if grid[i][y] == 'W':
                            break
                        if grid[i][y] == 'E':
                            cur += 1
                    for y in range(j + 1, n):
                        if grid[i][y] == 'W':
                            break
                        if grid[i][y] == 'E':
                            cur += 1
                    boom = max(boom, cur)

        return boom