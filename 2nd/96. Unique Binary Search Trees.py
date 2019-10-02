n = 5

dp = [0 for _ in range(n + 1)]

dp[1] = 1
dp[2] = 2

add = 1
for i in range(3, n + 1):
    dp[i] = dp[i - 1] * 2
    for j in range(i - 2, 0, -1):
        dp[i] += sum(dp[1:j + 1])
    for j in range(i - 3, 1, -1):
        dp[i] += dp[j]
print(dp)
