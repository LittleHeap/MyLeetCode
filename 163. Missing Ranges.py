nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99

temp = nums.copy()

while nums[0] < lower:
    nums.pop(0)
if lower not in nums:
    nums.insert(0, lower)

while nums[-1] > upper:
    nums.pop()
if upper not in nums:
    nums.append(upper)

res = []
for i in range(len(nums) - 1):
    if nums[i] + 1 == nums[i + 1]:
        continue
    else:
        cur = [nums[i] + 1, nums[i + 1] - 1]
        res.append(cur)

print(res)
ans = []
for ele in res:
    if len(set(ele)) == 1:
        cur = [ele[0]]
    else:
        cur = ele
    if cur[0] - 1 == lower and lower not in temp:
        cur.insert(0, lower)
    if cur[-1] + 1 == upper and upper not in temp:
        cur.append(upper)
    if len(cur) == 1:
        ans.append(str(cur[0]))
    else:
        ans.append(str(cur[0]) + '->' + str(cur[-1]))

print(ans)





