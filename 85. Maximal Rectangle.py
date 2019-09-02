matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]

m = len(matrix)
n = len(matrix[0])
ans = 0
height = 0

dp = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if matrix[i][j] == '1' and i - 1 == -1:
            dp[i][j] = 1
        elif matrix[i][j] == '1':
            dp[i][j] = dp[i - 1][j] + 1

for i in range(m):
    for j in range(n):
        if matrix[i][j] == '1':
            height = dp[i][j]
            ans = max(ans, height)
            width = 1
            while j + 1 < n and matrix[i][j + 1] == '1':
                height = min(height, dp[i][j + 1])
                width = width + 1
                ans = max(ans, height * width)
                j = j + 1

print(ans)