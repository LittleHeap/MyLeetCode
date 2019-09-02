points = [[3, 3], [5, -1], [-2, 4]]
K = 2

d = []
for i in range(len(points)):
    d.append((points[i][0]**2 + points[i][1]**2, i))

d = sorted(d, key=lambda x:x[0])

res = []
for i in range(K):
    res.append(points[d.pop(0)[1]])

print(res)