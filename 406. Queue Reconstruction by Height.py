people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]


people = sorted(people, reverse=True)

res = []
cur = []

for i, ele in enumerate(people):
    if i == 0:
        cur.append(ele)
    else:
        if ele[0] == cur[-1][0]:
            cur.append(ele)
        else:
            cur.reverse()
            for k in cur:
                res.insert(k[1], k)
            cur = [ele]
if cur:
    cur.reverse()
    for k in cur:
        res.insert(k[1], k)

print(res)
