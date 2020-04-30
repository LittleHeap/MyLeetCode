M = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


m = len(M)
n = len(M[0])


dp = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    dp[i][0] = 1
for j in range(n):
    dp[0][j] = 1

for i in range(1, m):
    for j in range(1, n):
        if M[i][j] != 1:
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

print(dp[-1][-1])


