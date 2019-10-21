matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

m = len(matrix)
n = len(matrix[0])

d = [[0 for _ in range(n)] for _ in range(m)]

for j in range(n):
    cur = 0
    for i in range(m):
        if matrix[i][j] == '1':
            cur += 1
            d[i][j] = cur
        else:
            cur = 0

res = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == '1':
            k = j + 1
            h = d[i][j]
            while k < n and matrix[i][k] == '1':
                h = min(h, d[i][k])
                res = max(res, h * (k - j + 1))
                k += 1

print(res)