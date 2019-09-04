nums = [1, 1, 2]
s = set()
n = len(nums)


def deep(cur, k, have):
    if k == n:
        s.add(tuple(cur))
        return
    for i in range(len(have)):
        newcur = cur.copy()
        newhave = have.copy()
        newcur.append(have[i])
        newhave.pop(i)
        deep(newcur, k + 1, newhave)


deep([], 0, nums)
res = []
for ele in s:
    res.append(list(ele))
print(res)
