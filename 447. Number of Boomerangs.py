import copy

points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]

d = {i: {} for i in range(len(points))}

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        d[i][dis] = d[i].get(dis, 0) + 1
        d[j][dis] = d[j].get(dis, 0) + 1

ans = 0

for i in range(len(points)):
    for ele in d.get(i).items():
        if ele[1] == 2:
            ans += 2
        elif ele[1] > 2:
            ans += (ele[1]) * (ele[1] - 1)

print(d)
print(ans)
