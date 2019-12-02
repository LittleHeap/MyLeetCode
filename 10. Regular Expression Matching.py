s = "mississippi"
p = "mis*is*p*."

s = list(s)
p = list(p)
s.insert(0, ' ')
p.insert(0, ' ')

n = len(s)
m = len(p)

l = max(m, n)

dp = [[0 for _ in range(l)] for _ in range(l)]
dp[0][0] = 1
print(dp)

for i in range(1, m):
        if p[i] == '.':
            for j in range(l):
                if j + 1 < n and dp[i - 1][j] > 0:
                    dp[i][j + 1] = 2
        elif p[i] == '*':
            for j in range(i + 1):
                if dp[i - 2][j] > 0:
                    dp[i][j] = dp[i - 2][j]
                if dp[i - 1][j] > 0:
                    for k in range(j - 1, i + 1):
                        dp[i][k] = max(dp[i][k], dp[i - 1][j])
        else:
            for j in range(l):
                if dp[i - 1][j] > 0:
                    if j + 1 < n and p[i] == s[j + 1]:
                        dp[i][j + 1] = 1

print(dp)