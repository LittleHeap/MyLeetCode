nums = [1, 0, -1, 0, -2, 2]
target = 0

nums.sort()

res = []
n = len(nums)

for i in range(n - 3):
    if i != 0 and nums[i] == nums[i - 1]:
        continue
    for j in range(i + 1, n - 2):
        if j != i + 1 and nums[j] == nums[j - 1]:
            continue
        l = j + 1
        r = n - 1
        while l < n and r >= 0 and l < r:
            s = nums[i] + nums[j] + nums[l] + nums[r]
            if s == target:
                res.append([nums[i], nums[j], nums[l], nums[r]])
                r -= 1
                while r >= 0 and nums[r] == nums[r + 1]:
                    r -= 1
                l += 1
                while l < n and nums[l] == nums[l - 1]:
                    l += 1
            elif s > target:
                r -= 1
                while r >= 0 and nums[r] == nums[r + 1]:
                    r -= 1
            else:
                l += 1
                while l < n and nums[l] == nums[l - 1]:
                    l += 1

print(res)