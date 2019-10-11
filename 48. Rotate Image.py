matrix = [[5, 1, 9, 11],
          [2, 4, 8, 10],
          [13, 3, 6, 7],
          [15, 14, 12, 16]
          ]

n = len(matrix)
times = n // 2


for t in range(times):
    left = t
    top = t
    right = n - t - 1
    bottom = n - t - 1
    for _ in range(n - 1 - t - t):
        print(matrix[0])
        print(matrix[1])
        print(matrix[2])
        print(matrix[3])
        print('------')
        cur = [left, top]
        while cur[1] <= right:
            if cur[1] == left:
                pre = matrix[cur[0]][cur[1]]
                cur[1] += 1
            else:
                matrix[cur[0]][cur[1]], pre = pre, matrix[cur[0]][cur[1]]
                cur[1] += 1
        cur[1] -= 1
        while cur[0] <= bottom:
            if cur[0] == top:
                cur[0] += 1
            else:
                matrix[cur[0]][cur[1]], pre = pre, matrix[cur[0]][cur[1]]
                cur[0] += 1
        cur[0] -= 1
        while cur[1] >= left:
            if cur[1] == right:
                cur[1] -= 1
            else:
                matrix[cur[0]][cur[1]], pre = pre, matrix[cur[0]][cur[1]]
                cur[1] -= 1
        cur[1] += 1
        while cur[0] >= top:
            if cur[0] == bottom:
                cur[0] -= 1
            else:
                matrix[cur[0]][cur[1]], pre = pre, matrix[cur[0]][cur[1]]
                cur[0] -= 1

print(matrix)
