import copy

candidates = [2]
target = 1

candidates.sort()
dp = [[] for _ in range(target)]

i = 0
hold = set()
while 1:
    if i > len(candidates) - 1:
        break
    else:
        if candidates[i] <= target:
            if candidates[i] in hold:
                i += 1
                continue
            left = copy.deepcopy(candidates)
            left.pop(i)
            dp[candidates[i] - 1] = [[[candidates[i]], left]]
            hold.add(candidates[i])
            i += 1
        else:
            break

candidates = candidates[:i]
print(candidates)
print(hold)
print(dp)

candidates = set(candidates)
for i in range(1, target + 1):
    for c in candidates:
        if i - c in hold:
            for prelist in dp[i - c - 1]:
                if c in prelist[1]:
                    a = copy.deepcopy(prelist[0])
                    b = copy.deepcopy(prelist[1])
                    a.append(c)
                    a.sort()
                    b.pop(b.index(c))
                    b.sort()
                    if [a, b] not in dp[i - 1]:
                        dp[i - 1].append([a, b])
                        hold.add(i)

print(dp[-1])
res = []
for ele in dp[-1]:
    res.append(ele[0])

print(res)