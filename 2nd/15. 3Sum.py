nums = [-2, 0, 1, 1, 2]

nums.sort()
print(nums)

n = len(nums)
res = set()

for i in range(n - 2):
    l = i + 1
    r = n - 1
    target = -nums[i]
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            res.add((nums[i], nums[l], nums[r]))
            l += 1
            r -= 1

ans = []
for ele in res:
    ans.append(list(ele))
print(ans)
