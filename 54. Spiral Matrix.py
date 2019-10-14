matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

m = len(matrix)
n = len(matrix[0])
i = 0
j = 0
row = set()
row.add(0)
row.add(m)
col = set()
col.add(-1)
col.add(n)
dir = 0

res = []
for _ in range(m * n):
    if dir == 0:
        res.append(matrix[i][j])
        j += 1
        if j in col:
            j -= 1
            i += 1
            dir += 1
            dir %= 4
            col.add(j)
    elif dir == 1:
        res.append(matrix[i][j])
        i += 1
        if i in row:
            i -= 1
            j -= 1
            dir += 1
            dir %= 4
            row.add(i)
    elif dir == 2:
        res.append(matrix[i][j])
        j -= 1
        if j in col:
            j += 1
            i -= 1
            dir += 1
            dir %= 4
            col.add(j)
    else:
        res.append(matrix[i][j])
        i -= 1
        if i in row:
            i += 1
            j += 1
            dir += 1
            dir %= 4
            row.add(i)

print(res)
