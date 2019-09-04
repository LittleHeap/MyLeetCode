import copy

candidates = [2]
target = 1

candidates.sort()

while 1 and len(candidates) > 0:
    if candidates[-1] > target:
        candidates.pop()
    else:
        break

res = set()


def deep(cur, have, remain):
    for i in range(len(have)):
        remain -= have[i]
        if remain < 0:
            return
        newcur = copy.deepcopy(cur)
        newcur.append(have[i])
        newhave = copy.deepcopy(have)
        newhave = newhave[i + 1:]
        if remain == 0:
            newcur.sort()
            res.add(tuple(newcur))
            return
        deep(newcur, newhave, remain)
        remain += have[i]


deep([], candidates, target)

ans = []
for ele in res:
    ans.append(list(ele))

print(ans)
