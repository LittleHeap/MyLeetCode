class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        hold = set()

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        done = set()

        def dfs(i, j, cur, origin):
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x < 0 or x >= m or y < 0 or y >= n or (x, y) in done or grid[x][y] == 0:
                    continue
                else:
                    done.add((x, y))
                    cur.append((x - origin[0], y - origin[1]))
                    dfs(x, y, cur, origin)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in done:
                    now = [(0, 0)]
                    done.add((i, j))
                    dfs(i, j, now, (i, j))
                    hold.add(tuple(now))

        return len(hold)