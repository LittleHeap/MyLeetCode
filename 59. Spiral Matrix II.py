n = 5

res = [[0 for _ in range(n)] for _ in range(n)]

dir = [0, 1, 2, 3]
row = set()
col = set()
row.add(n)
row.add(0)
col.add(n)
col.add(-1)

i = 0
j = 0
index = 0

for num in range(n ** 2):
    print(res)
    print([i, j])
    print(i)
    res[i][j] = num + 1
    if dir[index % 4] == 0:
        j += 1
        if j in col:
            j -= 1
            col.add(j)
            i += 1
            index += 1
    elif dir[index % 4] == 1:
        i += 1
        if i in row:
            i -= 1
            row.add(i)
            j -= 1
            index += 1
    elif dir[index % 4] == 2:
        j -= 1
        if j in col:
            j += 1
            col.add(j)
            i -= 1
            index += 1
    elif dir[index % 4] == 3:
        i -= 1
        if i in row:
            i += 1
            row.add(i)
            j += 1
            index += 1

print(res)
