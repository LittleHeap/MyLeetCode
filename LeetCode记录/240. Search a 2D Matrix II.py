import heapq

matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 17

m = len(matrix)
n = len(matrix[0])
res = set()
heap = []
have = set()

heapq.heappush(heap, (matrix[0][0], [0, 0]))
have.add(0)
while heap:
    print(heap)
    print(have)
    cur = heapq.heappop(heap)
    if cur[0] == target:
        res.add(True)
        break
    elif cur[0] < target:
        if cur[1][0] + 1 < m and (cur[1][0] + 1) * m + cur[1][1] not in have:
            heapq.heappush(heap, (matrix[cur[1][0] + 1][cur[1][1]], [cur[1][0] + 1, cur[1][1]]))
            have.add((cur[1][0] + 1) * m + cur[1][1])
        if cur[1][1] + 1 < n and cur[1][0] * m + cur[1][1] + 1 not in have:
            heapq.heappush(heap, (matrix[cur[1][0]][cur[1][1] + 1], [cur[1][0], cur[1][1] + 1]))
            have.add(cur[1][0] * m + cur[1][1] + 1)
print(res)
