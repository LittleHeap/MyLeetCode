s = ")("

dp = [set() for _ in range(len(s) + 1)]

dp[0].add((0, 0, ''))
print(dp)

for i in range(1, len(s) + 1):
    if s[i - 1] in ['(', ')']:
        for ele in dp[i - 1]:
            dp[i].add(ele)
            if s[i - 1] == '(':
                dp[i].add((ele[0] + 1, ele[1], ele[2] + '('))
            else:
                if ele[0] > ele[1]:
                    dp[i].add((ele[0], ele[1] + 1, ele[2] + ')'))
    else:
        for ele in dp[i - 1]:
            dp[i].add((ele[0], ele[1], ele[2] + s[i - 1]))

print(dp[-1])
temp = []
m = 0
for ele in dp[-1]:
    if ele[0] == ele[1]:
        m = max(m, ele[0])
        temp.append([ele[2], ele[0]])
res = []
for ele in temp:
    if ele[1] == m:
        res.append(ele[0])
print(res)