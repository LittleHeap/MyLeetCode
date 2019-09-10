import copy
n = 4
k = 9

save = {}
nums = [i + 1 for i in range(n)]

s = 1
save[0] = 1
for i in range(n - 1):
    s = s * (i + 1)
    save[i + 1] = s

print(save)
res = []

for i in range(1, n + 1):
    back = n - i
    cur = (k - 1) // save.get(back)
    k -= cur * save.get(back)
    res.append(str(nums[cur]))
    nums.remove(nums[cur])

print(res)