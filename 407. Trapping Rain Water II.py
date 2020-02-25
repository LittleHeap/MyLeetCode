heightMap = [[78, 16, 94, 36], [87, 93, 50, 22], [63, 28, 91, 60], [64, 27, 41, 27], [73, 37, 12, 69], [68, 30, 83, 31],
             [63, 24, 68, 36]]

m = len(heightMap)
n = len(heightMap[0])

temp = [[float('inf') for _ in range(n)] for _ in range(m)]

for i in range(1, m - 1):
    t = heightMap[i][0]
    for j in range(1, n - 1):
        temp[i][j] = min(temp[i][j], t)
        t = max(t, heightMap[i][j])
    t = heightMap[i][-1]
    for j in range(n - 2, 0, -1):
        temp[i][j] = min(temp[i][j], t)
        t = max(t, heightMap[i][j])
for j in range(1, n - 1):
    t = heightMap[0][j]
    for i in range(1, m - 1):
        temp[i][j] = min(temp[i][j], t)
        t = max(t, heightMap[i][j])
    t = heightMap[-1][j]
    for i in range(m - 2, 0, -1):
        temp[i][j] = min(temp[i][j], t)
        t = max(t, heightMap[i][j])

print(temp)

res = 0
for i in range(1, m - 1):
    for j in range(1, n - 1):
        cur = temp[i][j] - heightMap[i][j]
        if cur > 0:
            continue
        else:
            temp[i][j] = float('inf')

print(temp)


def deep(i, j, p, q):
    p.append(heightMap[i][j])
    q.append(temp[i][j])
    temp[i][j] = float('inf')
    if i + 1 < m and temp[i + 1][j] != float('inf'):
        deep(i + 1, j, p, q)
    if j + 1 < n and temp[i][j + 1] != float('inf'):
        deep(i, j + 1, p, q)
    if i - 1 >= 0 and temp[i - 1][j] != float('inf'):
        deep(i - 1, j, p, q)
    if i - 1 >= 0 and temp[i][j - 1] != float('inf'):
        deep(i, j - 1, p, q)


res = 0
for i in range(1, m - 1):
    for j in range(1, n - 1):
        if temp[i][j] != float('inf'):
            p = []
            q = []
            cur = deep(i, j, p, q)
            h = min(q)
            print(p)
            print(q)
            for ele in p:
                res += h - ele

print(res)
