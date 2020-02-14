class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ob = set()
        building = set()

        get = set()

        for i in range(m):
            for j in range(n):
                get.add((i, j))
                if grid[i][j] == 1:
                    building.add((i, j))
                elif grid[i][j] == 2:
                    ob.add((i, j))

        done = building ^ ob

        def bfs(start):
            now = set()
            queue = [start]
            step = 1
            while queue:
                newqueue = []
                while queue:
                    current = queue.pop()
                    i = current[0]
                    j = current[1]
                    if i + 1 < m and (i + 1, j) not in done:
                        grid[i + 1][j] += step
                        done.add((i + 1, j))
                        newqueue.append((i + 1, j))
                        now.add((i + 1, j))
                    if j + 1 < n and (i, j + 1) not in done:
                        grid[i][j + 1] += step
                        done.add((i, j + 1))
                        newqueue.append((i, j + 1))
                        now.add((i, j + 1))
                    if i - 1 >= 0 and (i - 1, j) not in done:
                        grid[i - 1][j] += step
                        done.add((i - 1, j))
                        newqueue.append((i - 1, j))
                        now.add((i - 1, j))
                    if j - 1 >= 0 and (i, j - 1) not in done:
                        grid[i][j - 1] += step
                        done.add((i, j - 1))
                        newqueue.append((i, j - 1))
                        now.add((i, j - 1))
                step += 1
                queue = newqueue
            return now

        for ele in building:
            done = building ^ ob
            can = bfs(ele)
            get = get & can

        res = float('inf')

        done = building ^ ob
        for i in range(m):
            for j in range(n):
                if (i, j) in get:
                    res = min(res, grid[i][j])

        if res == 0 or res == float('inf'):
            return -1
        else:
            return res