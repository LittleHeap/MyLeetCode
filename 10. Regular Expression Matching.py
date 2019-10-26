s = "aab"
p = "c*a*b"

m = len(p)
n = len(s)

dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
dp[0][0] = 1
print(dp)

j = 1
for i in range(1, m + 1):
    if p[i] == '.':
        if dp[i - 1][j - 1] == 1:
            dp[i][j] = 2
            j += 1
        else:
            break
    elif p[i] == '*':
        if dp[i - 1][j - 1] == 2:
            dp[i][j - 2] = 1
            for t in range(j - 1, n + 1):
                dp[i][t] = 2
        elif dp[i - 1][j - 1] == 1:
            for t in range(j - 2, n + 1):
                dp[i][t] = 1
        else:
            dp[i][j - 2] = 1

    elif p[i - 1] == s[j - 1]:
        if dp[i - 1][j - 1] == 1:
            dp[i][j] = 1
        else:
            break
    else:
        pass
    if j == n + 1:
        break

print(dp)
