n = 4

col = {}
pie = {}
na = {}
ans = []


def deep(i, col, pie, na):
    for j in range(n):
        newcol = col.copy()
        newpie = pie.copy()
        newna = na.copy()
        if newcol.get(j) is None and newpie.get(i + j) is None and newna.get(j - i) is None:
            newcol[j] = 1
            newpie[i + j] = 1
            newna[j - i] = 1
            print([i, j])
            if i < n - 1:
                deep(i + 1, newcol, newpie, newna)
            else:
                ans.append(1)
    return


deep(0, col, pie, na)
print(ans)
