obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

m = len(obstacleGrid)
n = len(obstacleGrid[0])

dp = [[0 for _ in range(n)] for _ in range(m)]

for j in range(n):
    if obstacleGrid[0][j] == 0:
        dp[0][j] = 1
    else:
        break

for i in range(m):
    if obstacleGrid[i][0] == 0:
        dp[i][0] = 1
    else:
        break

for i in range(1, m):
    for j in range(1, n):
        if obstacleGrid[i][j] == 1:
            continue
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j - 1]

print(dp)
print(dp[-1][-1])