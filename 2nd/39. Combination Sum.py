import copy
candidates = [1,2]
target = 1

dp = [[] for _ in range(target)]
ke = set()
ke.add(0)
for ele in candidates:
    dp[ele - 1].append([ele])
    ke.add(ele)
print(dp)
print(ke)

for i in range(1, target + 1):
    print(i)
    for ele in candidates:
        if i - ele in ke and i - ele != 0 and i - ele != i:
            ke.add(i)
            for found in dp[i - ele - 1]:
                cur = copy.deepcopy(found)
                cur.append(ele)
                cur.sort()
                if cur not in dp[i - 1]:
                    dp[i - 1].append(cur)

    print(dp)

print(dp)
