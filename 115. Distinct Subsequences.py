s = "eee"
t = "eee"

m = len(s)
n = len(t)

dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(m + 1):
    dp[i][0] = 1

for k in range(1, n + 1):
    if s[k - 1] == t[k - 1]:
        dp[k][k] = 1
    else:
        for p in range(k, n + 1):
            dp[k][k] = 0
        break

for i in range(2, m + 1):
    if i <= n:
        stop = i
    else:
        stop = n + 1
    for j in range(1, stop):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j]


print(dp)
