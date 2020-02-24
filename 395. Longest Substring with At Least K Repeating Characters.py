s = "bbaaacbd"
k = 3

ans = 0
dp = [{} for _ in range(len(s))]

for i in range(len(s)):
    if i > 0:
        dp[i] = dp[i - 1].copy()
    dp[i][s[i]] = dp[i].get(s[i], 0) + 1

    temp = [ele for ele in dp[i].values() if ele < k]
    if not temp:
        ans = i + 1
    else:
        for j in range(i - 1):
            temp = dp[i].copy()
            for key in dp[j]:
                temp[key] -= dp[j][key]
            print(temp)
            now = [ele for ele in temp.values() if (ele < k and ele > 0)]
            print(now)
            if not now:
                ans = max(ans, i - j)
                break

print(dp)
print(ans)
