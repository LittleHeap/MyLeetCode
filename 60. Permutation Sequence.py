import copy

n = 6
k = 67

save = []
cur = 1
for i in range(1, n + 1):
   cur *= i
   save.append(cur)
print(save)

hold = [str(i) for i in range(1, n + 1)]
print(hold)

index = 0
res = []
last = n

for i in range(n):
    if k == 1:
        res.extend(hold)
        break
    index = 0
    while save[index] < k:
        index += 1
    index -= 1
    for _ in range(last - index - 2):
        res.append(hold.pop(0))
    last = index + 1
    can = (k - 1) // save[index]
    res.append(hold[can])
    k -= can * save[index]
    hold.pop(can)

print(res)