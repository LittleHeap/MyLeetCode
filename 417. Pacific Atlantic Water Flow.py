matrix = [[1, 2, 2, 3, 5],
          [3, 2, 3, 4, 4],
          [2, 4, 5, 3, 1],
          [6, 7, 1, 4, 5],
          [5, 1, 1, 2, 4]]

m = len(matrix)
n = len(matrix[0])

p = [[0 for _ in range(n)] for _ in range(m)]
a = [[0 for _ in range(n)] for _ in range(m)]


def dfs(ocean, i, j):
    ocean[i][j] = 1
    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if (x < 0 or x >= m or y < 0 or y >= n) or matrix[i][j] > matrix[x][y] or ocean[x][y]:
            continue
        else:
            dfs(ocean, x, y)


for i in range(m):
    dfs(p, i, 0)
    dfs(a, i, n - 1)

for j in range(n):
    dfs(p, 0, j)
    dfs(a, m - 1, j)

res = []
for i in range(m):
    for j in range(n):
        if a[i][j] and p[i][j]:
            res.append([[i, j]])

print(res)
