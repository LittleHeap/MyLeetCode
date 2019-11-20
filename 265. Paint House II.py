import heapq

costs = [[1, 5, 3], [2, 9, 4]]

n = len(costs)
k = len(costs[0])
pre = []
for i in range(n):
    if i == 0:
        for c in costs[i]:
            heapq.heappush(pre, c)
    else:
        newpre = []
        for j in range(k):
            if pre[0] != costs[i - 1][j]:
                heapq.heappush(newpre, costs[i][j] + pre[0])
                costs[i][j] += pre[0]
            else:
                temp = heapq.heappop(pre)
                heapq.heappush(newpre, costs[i][j] + pre[0])
                costs[i][j] += pre[0]
                heapq.heappush(pre, temp)
        pre = newpre

print(pre)
