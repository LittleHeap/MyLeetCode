import copy

points = [[0, 0], [1, 0], [2, 0]]

d = {}
h = set()

ans = 0
for i in range(len(points)):
    for j in range(len(points) - 1):
        if j == i:
            continue
        for k in range(j + 1, len(points)):
            if k == i:
                continue
            if (i, j) not in h:
                i_j = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                d[(i, j)] = i_j
                d[(j, i)] = i_j
                h.add((i, j))
                h.add((j, i))
            else:
                i_j = d.get((i, j))
            if (i, k) not in h:
                i_k = (points[i][0] - points[k][0]) ** 2 + (points[i][1] - points[k][1]) ** 2
                d[(i, k)] = i_k
                d[(k, i)] = i_k
                h.add((i, k))
                h.add((k, i))
            else:
                i_k = d.get((i, k))
            if i_j == i_k:
                ans += 1
print(ans * 2)
