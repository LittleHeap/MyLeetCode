n = 5

row = set()
row.add(0)
row.add(n)
col = set()
col.add(n)
col.add(-1)
dir = 0
res = [[0 for _ in range(n)] for _ in range(n)]

i = 0
j = 0

for num in range(n ** 2):
    res[i][j] = num + 1
    if dir % 4 == 0:
        j += 1
        if j in col:
            j -= 1
            col.add(j)
            i += 1
            dir += 1
    elif dir % 4 == 1:
        i += 1
        if i in row:
            i -= 1
            row.add(i)
            j -= 1
            dir += 1
    elif dir % 4 == 2:
        j -= 1
        if j in col:
            j += 1
            col.add(j)
            i -= 1
            dir += 1
    elif dir % 4 == 3:
        i -= 1
        if i in row:
            i += 1
            row.add(i)
            j += 1
            dir += 1

print(res)
