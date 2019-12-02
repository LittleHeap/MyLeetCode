m = 2
n = 2
positions = [[0, 0], [1, 1], [0, 1]]

res = []
ans = []
done = set()
have = set()

for po in positions:
    have.add((po[0], po[1]))
    if (po[0] - 1, po[1]) not in have and (po[0] + 1, po[1]) not in have and (po[0], po[1] - 1) not in have and (
                po[0], po[1] + 1) not in have:
        s = set()
        s.add((po[0],po[1]))
        res.append(s)
        ans.append(len(res))
        continue
    if (po[0], po[1]) in done:
        ans.append(len(res))
        continue
    else:
        done.add((po[0], po[1]))
    index = []
    newres = []
    cur = set()
    cur.add((po[0], po[1]))
    for i in range(len(res)):
        if (po[0] - 1, po[1]) in res[i] or (po[0] + 1, po[1]) in res[i] or (po[0], po[1] - 1) in res[i] or (
                po[0], po[1] + 1) in res[i]:
            cur = cur | res[i]
        else:
            newres.append(res[i])
    newres.append(cur)
    ans.append(len(newres))
    res = newres

print(ans)
