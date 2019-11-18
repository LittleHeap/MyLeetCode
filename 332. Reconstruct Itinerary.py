import copy

tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]

d = {}
for t in tickets:
    if t[0] not in d:
        d[t[0]] = [t[1]]
    else:
        d[t[0]].append(t[1])

for ele in d:
    d[ele].sort()

print(d)
res = []


def deep(cur, d):
    if res:
        return
    if not d:
        res.extend(cur)
    start = cur[-1]
    if start not in d:
        return
    for i in range(len(d[start])):
        newd = copy.deepcopy(d)
        newcur = copy.deepcopy(cur)
        newcur.append(newd[start].pop(i))
        if not newd[start]:
            newd.pop(start)
        deep(newcur, newd)


deep(['JFK'], d)
print(res)
