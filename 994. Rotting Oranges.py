class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        temp = [[float('inf') for _ in range(n)] for _ in range(m)]

        def bfs(a, b, step):
            cur = [(a, b)]
            while cur:
                newcur = []
                while cur:
                    (i, j) = cur.pop()
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if x < 0 or x >= m or y < 0 or y >= n:
                            continue
                        else:
                            if grid[x][y] == 1 and temp[x][y] > step + 1:
                                temp[x][y] = step + 1
                                newcur.append((x, y))
                cur = newcur
                step += 1

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    bfs(row, col, 0)

        res = 0
        print(temp)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if temp[i][j] == float('inf'):
                        return -1
                    else:
                        res = max(res, temp[i][j])

        return res




