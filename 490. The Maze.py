class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        m = len(maze)
        n = len(maze[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]
        self.possible = False

        def bfs(x, y):
            if x == destination[0] and y == destination[1]:
                self.possible = True
                return

            if visited[x][y] == 1 or self.possible:
                return

            visited[x][y] = 1

            # top
            x_, y_ = x, y

            while x_ - 1 >= 0 and maze[x_ - 1][y_] == 0:
                x_ -= 1

            if x_ != x:
                bfs(x_, y_)

            # right
            x_, y_ = x, y

            while y_ + 1 < n and maze[x_][y_ + 1] == 0:
                y_ += 1

            if y_ != y:
                bfs(x_, y_)

            # bottom
            x_, y_ = x, y

            while x_ + 1 < m and maze[x_ + 1][y_] == 0:
                x_ += 1

            if x_ != x:
                bfs(x_, y_)

            # left
            x_, y_ = x, y

            while y_ - 1 >= 0 and maze[x_][y_ - 1] == 0:
                y_ -= 1

            if y_ != y:
                bfs(x_, y_)

        bfs(start[0], start[1])

        return self.possible