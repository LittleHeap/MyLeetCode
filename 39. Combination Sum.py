candidates = [2, 3, 5]
target = 8

candidates.sort()
for i in range(len(candidates)):
    if candidates[i] > target:
        candidates = candidates[:i]
        break

dp = [[] for _ in range(target + 1)]
print(dp)

have = set()
for ele in candidates:
    dp[ele].append([ele])
    have.add(ele)
print(dp)

for i in range(1, target + 1):
    for ele in candidates:
        if ele >= i:
            break
        else:
            if (i - ele) in have:
                have.add(i)
                for h in dp[i - ele]:
                    new = h.copy()
                    new.append(ele)
                    new.sort()
                    if new not in dp[i]:
                        dp[i].append(new)

print(dp)

