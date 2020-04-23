class Solution:
    def shortestDistance(self, maze: List[List[int]], s: List[int], d: List[int]) -> int:

        m = len(maze)
        n = len(maze[0])

        f = {}
        f[(s[0], s[1])] = 0

        q = [(0, s[0], s[1])]

        while q:
            dist, i, j = heapq.heappop(q)
            if i == d[0] and j == d[1]:
                return dist
            else:
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newi, newj, newdist = i, j, dist
                    while newi + x < m and newi + x >= 0 and newj + y < n and newj + y >= 0 and maze[newi + x][
                        newj + y] != 1:
                        newi += x
                        newj += y
                        newdist += 1
                    if (newi, newj) not in f or newdist < f[(newi, newj)]:
                        f[(newi, newj)] = newdist
                        q.append((newdist, newi, newj))
        return -1
