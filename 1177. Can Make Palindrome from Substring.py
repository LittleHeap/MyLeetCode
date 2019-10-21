s = "berilmre"
queries = [[1,6,2],[6,7,0],[7,7,1]]

res = []
for ele in queries:
    curs = s[ele[0]:ele[1] + 1]
    k = ele[2]
    d = {}
    for i in range(len(curs)):
        d[curs[i]] = d.get(curs[i],0) + 1
    c = 0
    print(d)
    for case in d.items():
        if case[1] % 2 == 1:
            c += 1
    if c // 2 <= k or c == 1:
        res.append(True)
    else:
        res.append(False)


print(res)
