A = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]

col = [0 for _ in range(len(A[0]))]

for row in A:
    if row[0] == 0:
        for i in range(len(row)):
            row[i] = 1 - row[i]
            col[i] = col[i] + row[i]
    else:
        for i in range(len(row)):
            col[i] = col[i] + row[i]

print(col)

ans = 0
for i in range(len(A[0])):
    cur = col.pop()
    m = max(cur, len(A) - cur)
    now = 2 ** i
    ans = ans + now * m

print(ans)