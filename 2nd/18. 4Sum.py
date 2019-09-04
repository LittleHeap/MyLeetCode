nums = [-1, 0, -5, -2, -2, -4, 0, 1, -2]
target = -9

nums.sort()

n = len(nums)
res = []

for i in range(n - 3):
    if i > 0 and nums[i] == nums[i - 1]:
        # 记得每一层都要审核重复元素
        continue
    for j in range(i + 1, n - 2):
        if j > i + 1 and nums[j] == nums[j - 1]:
            # 记得每一层都要审核重复元素
            continue
        l = j + 1
        r = n - 1
        t = target - nums[i] - nums[j]
        while l < r:
            if nums[l] + nums[r] > t:
                r -= 1
            elif nums[l] + nums[r] < t:
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    # 记得每一层都要审核重复元素
                    l += 1
            else:
                res.append([nums[i], nums[j], nums[l], nums[r]])
                l += 1
                r -= 1
                # 即使找到答案，仍然继续遍历
                while l < r and nums[l] == nums[l - 1]:
                    # 记得每一层都要审核重复元素
                    l += 1

print(res)
