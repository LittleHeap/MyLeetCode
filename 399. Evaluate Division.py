equations = [["a", "b"], ["e", "f"], ["b", "e"]]
values = [3.4, 1.4, 2.3]
queries = [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]

d = {}

for i in range(len(equations)):
    if equations[i][0] not in d:
        d[equations[i][0]] = {}
    if equations[i][1] not in d:
        d[equations[i][1]] = {}
    d[equations[i][0]][equations[i][1]] = values[i]
    d[equations[i][1]][equations[i][0]] = 1 / values[i]




def deep(char, v, target):
    if value[0] is not None:
        return
    if char == target:
        value[0] = v
        return
    for ele in d[char]:
        if ele not in done:
            done.add(ele)
            deep(ele, v * d[char][ele], target)


res = []
for q in queries:
    if q[0] not in d or q[1] not in d:
        res.append(float(-1))
    elif q[0] == q[1]:
        res.append(float(1))
    else:
        done = set()
        done.add(q[0])
        value = [None]
        deep(q[0], 1, q[1])
        res.append(value[0])

print(res)

