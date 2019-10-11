import copy

candidates = [2, 5, 2, 1, 2]
target = 5

candidates.sort()
for i in range(len(candidates)):
    if candidates[i] > target:
        candidates = candidates[: i]
        break

dp = [[[], []] for _ in range(target + 1)]
have = set()
for ele in set(candidates):
    have.add(ele)
    dp[ele][0].append([ele])
    can = candidates.copy()
    can.remove(ele)
    dp[ele][1].append(set(can))

hold = set(candidates)
for i in range(1, target + 1):
    for h in hold:
        if h > i:
            break
        if (i - h) in have:
            for index in range(len(dp[i - h][0])):
                if h in dp[i - h][1][index]:
                    newl = dp[i - h][0][index].copy()
                    newl.append(h)
                    news = candidates.copy()
                    newl.sort()
                    if newl not in dp[i][0]:
                        for p in newl:
                            news.remove(p)
                        dp[i][0].append(newl)
                        dp[i][1].append(set(news))
                        have.add(i)
print(dp)
print(dp[-1][0])
