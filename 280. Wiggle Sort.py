nums = [3, 5, 2, 1, 6, 4]

n = len(nums)

for i in range(1, n, 2):
    if i == n - 1:
        if nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
    else:
        if max(nums[i - 1:i + 2]) != nums[i]:
            if nums[i - 1] >= nums[i + 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            else:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

print(nums)