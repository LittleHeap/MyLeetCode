m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1]]

grid = [[0 for _ in range(n)] for _ in range(m)]

for ele in positions:
    grid[ele[0]][ele[1]] = 1

print(grid)

done = set()
island = {}
mark = {}


def dfs(i, j, number):
    mark[(i, j)] = number
    if i + 1 < m and (i + 1, j) not in done and grid[i + 1][j] == 1:
        island[number].append((i + 1, j))
        done.add((i + 1, j))
        dfs(i + 1, j, number)
    if j + 1 < n and (i, j + 1) not in done and grid[i][j + 1] == 1:
        island[number].append((i, j + 1))
        done.add((i, j + 1))
        dfs(i, j + 1, number)


number = 1
for i in range(m):
    for j in range(n):
        if grid[i][j] == 1 and (i, j) not in done:
            island[number] = [(i, j)]
            dfs(i, j, number)
            number += 1

print(island)
print(mark)

total = len(island)
res = []
for index in range(len(positions) - 1, -1, -1):
    res.append(total)
    m = mark[(positions[index][0], positions[index][1])]
    island[m].pop()
    if not island[m]:
        total -= 1

res.reverse()
print(res)
