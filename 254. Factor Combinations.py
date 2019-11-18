n = 7

res = []


def deep(num, cur):
    print(num)
    if num == 2 or num == 1:
        newcur = cur.copy()
        if num == 2:
            newcur.append(2)
        newcur.sort()
        if newcur not in res:
            res.append(newcur)
        return
    for i in range(2, n):
        if num % i == 0:
            newcur = cur.copy()
            newcur.append(i)
            deep(num // i, newcur)


deep(n, [])
print(res)
