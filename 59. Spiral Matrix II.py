n = 5

res = [[0 for _ in range(n)] for _ in range(n)]

dir = 0
row = set()
row.add(0)
row.add(n)
col = set()
col.add(-1)
col.add(n)

i, j = 0, 0
for k in range(1, n * n + 1):
    print([i,j])
    res[i][j] = k
    if dir == 0:
        j += 1
        if j in col:
            j -= 1
            i += 1
            dir += 1
            dir %= 4
            col.add(j)
    elif dir == 1:
        i += 1
        if i in row:
            i -= 1
            j -= 1
            dir += 1
            dir %= 4
            row.add(i)
    elif dir == 2:
        j -= 1
        if j in col:
            j += 1
            i -= 1
            dir += 1
            dir %= 4
            col.add(j)
    else:
        i -= 1
        if i in row:
            i += 1
            j += 1
            dir += 1
            dir %= 4
            row.add(i)
print(res)

