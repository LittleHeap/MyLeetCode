import copy
n = 4

col = set()
pie = set()
na = set()
res = []

def deep(i, col, pie, na, cur):
    if i == n:
        res.append(cur)
        return
    for j in range(n):
        if j not in col and j - i not in pie and j + i not in na:
            temp = ['.' for _ in range(n)]
            temp[j] = 'Q'
            temp = ''.join(temp)
            newcur = copy.deepcopy(cur)
            newcol = copy.deepcopy(col)
            newpie = copy.deepcopy(pie)
            newna = copy.deepcopy(na)
            newcur.append(temp)
            newcol.add(j)
            newpie.add(j - i)
            newna.add(j + i)
            deep(i + 1, newcol, newpie, newna, newcur)


deep(0, col, pie, na, [])
print(res)
