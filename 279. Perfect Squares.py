n = 13

hold = []
for i in range(1, n+1):
    if i ** 2 > n:
        break
    else:
        hold.append(i ** 2)

print(hold)

dp = [float('inf') for _ in range(n)]
for ele in hold:
    dp[ele - 1] = 1

for i in range(1, n + 1):
    for step in hold:
        if i + step - 1 < n:
            dp[i + step - 1] = min(dp[i + step - 1], dp[i - 1] + 1)

print(dp)

