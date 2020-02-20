import copy

m = 1
n = 3

d = {1: [2, 4, 5, 6, 8], 2: [1, 3, 4, 5, 6, 7, 9], 3: [2, 4, 5, 6, 8], 4: [1, 2, 3, 5, 7, 8, 9],
     5: [1, 2, 3, 4, 6, 7, 8, 9], 6: [1, 2, 3, 5, 7, 8, 9], 7: [2, 4, 5, 6, 8], 8: [1, 3, 4, 5, 6, 7, 9],
     9: [2, 4, 5, 6, 8]}

res = [0]


def deep(node, done, l):
    if len(done) == l:
        res[0] += 1
        return
    for ele in d[node]:
        if ele not in done:
            newdone = copy.deepcopy(done)
            newdone.add(ele)
            deep(ele, newdone, l)


for i in range(m, n + 1):
    for start in range(1, 10):
        done = set()
        done.add(start)
        deep(start, done, i)

print(res[0])
