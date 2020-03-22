class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        res = [0]
        done = set()
        m = len(grid)
        n = len(grid[0])

        def deep(i, j):
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x < 0 or x >= m or y < 0 or y >= n:
                    res[0] += 1
                    continue
                else:
                    if (x, y) not in done and grid[x][y] == 1:
                        done.add((x, y))
                        deep(x, y)
                    elif (x, y) not in done and grid[x][y] == 0:
                        res[0] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    done.add((i, j))
                    deep(i, j)
                    return res[0]