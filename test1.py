import collections
n = 7
model = [7,10,1,2,7,7,1]


target = (n + 1) // 2
hold = collections.Counter(model)

hold = sorted(hold.items(), key=lambda x:x[1], reverse = True)

res = 0
cur = 0
for number, times in hold:
    cur += times
    res += 1
    if cur >= target:
        break


print(res)