nums = [1, 5, 1, 1, 6, 4, 7]

n = len(nums)
nums.sort()

index = n // 2
while index != 0:
    nums.insert(index, nums.pop())
    index -= 1

print(nums)