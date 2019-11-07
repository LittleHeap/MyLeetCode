a = [["a", "c", "a", "b", "b"],
     ["c", "b", "a", "c", "b"],
     ["a", "a", "e", "c", "b"],
     ["b", "b", "d", "a", "g"],
     ["a", "b", "e", "b", "a"]]

n = len(a)
d = {}

for i in range(n - 1, 0, - 1):
    p = i
    q = 0
    cur = ''
    for _ in range(n):
        cur += a[p][q]
        p += 1
        q += 1
        if p == n:
            p = i
            q = 0
    if cur in d:
        d[cur].append(n - i)
    else:
        d[cur] = [n - i]

for j in range(n):
    p = 0
    q = j
    cur = ''
    for _ in range(n):
        cur += a[p][q]
        p += 1
        q += 1
        if q == n:
            p = 0
            q = j
    if cur in d:
        d[cur].append(j + n)
    else:
        d[cur] = [j + n]

temp = sorted(d.items(), key=lambda x: x[0])
res = []
for ele in temp:
    res.extend(ele[1])

print(res)
