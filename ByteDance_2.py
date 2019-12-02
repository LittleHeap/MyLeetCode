rooms = [[float('inf'), -1, 0, float('inf')], [float('inf'), float('inf'), float('inf'), -1],
         [float('inf'), -1, float('inf'), -1], [0, -1, float('inf'), float('inf')]]

m = len(rooms)
n = len(rooms[0])

for x in range(m):
    for y in range(n):
        if rooms[x][y] == 0:
            queue = []
            queue.append((x, y))
            step = 0
            done = set()
            done.add((x, y))
            while queue:
                newqueue = []
                step += 1
                for ele in queue:
                    i = ele[0]
                    j = ele[1]
                    if i - 1 >= 0 and (i - 1, j) not in done and rooms[i - 1][j] > step:
                        rooms[i - 1][j] = step
                        newqueue.append([i - 1, j])
                        done.add((i - 1, j))
                    if i + 1 < m and (i + 1, j) not in done and rooms[i + 1][j] > step:
                        rooms[i + 1][j] = step
                        newqueue.append([i + 1, j])
                        done.add((i + 1, j))
                    if j - 1 >= 0 and (i, j - 1) not in done and rooms[i][j - 1] > step:
                        rooms[i][j - 1] = step
                        newqueue.append([i - 1, j])
                        done.add((i, j - 1))
                    if j + 1 < n and (i, j + 1) not in done and rooms[i][j + 1] > step:
                        rooms[i][j + 1] = step
                        newqueue.append([i, j + 1])
                        done.add((i, j + 1))
                queue = newqueue

print(rooms)
