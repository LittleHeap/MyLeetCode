s = "1010101112323417"
dp = [[0, 0] for _ in range(len(s) + 1)]

dp[1] = [1, 0]

for i in range(2, len(s) + 1):
    if s[i - 1] == '0':
        dp[i][0] = 0
    else:
        dp[i][0] = sum(dp[i - 1])

    if s[i - 1] == '0':
        if s[i - 2] == '1' or s[i - 2] == '2':
            dp[i][0] = sum(dp[i - 2])
            if i == 2:
                dp[i][1] += 1
        else:
            print(0)
    else:
        if int(s[i - 2]) == 0:
            dp[i][1] = 0
        elif int(s[i - 2]) * 10 + int(s[i - 1]) <= 26:
            dp[i][1] = sum(dp[i - 2])
            if i == 2:
                dp[i][1] += 1
        else:
            dp[i][1] = 0

print(dp)
print(sum(dp[-1]))
