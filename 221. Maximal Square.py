matrix = [["1", "0", "1", "0"], ["1", "0", "1", "1"], ["1", "0", "1", "1"], ["1", "1", "1", "1"]]

m = len(matrix)
n = len(matrix[0])

mat = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if matrix[i][j] == '1':
            if i - 1 >= 0:
                mat[i][j] = mat[i - 1][j] + 1
            else:
                mat[i][j] = 1

print(mat)
ans = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == '1':
            ans = max(ans, 1)
            height = mat[i][j]
            for k in range(j + 1, n):
                if matrix[i][k] == '1':
                    height = min(height, mat[i][k])
                    width = k + 1 - j
                    ans = max(ans, min(height, width) ** 2)
                    if width > height:
                        break
                else:
                    break

print(ans)
