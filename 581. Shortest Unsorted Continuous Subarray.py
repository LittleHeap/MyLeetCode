nums = [1, 2, 3, 5, 4]

another = nums.copy()
another.sort()
print(another)

l = 1
r = 1
left = 0
right = len(nums) - 1

while left < right and (l or r):
    if l and another[left] == nums[left]:
        left += 1
    else:
        l = 0
    if r and another[right] == nums[right]:
        right -= 1
    else:
        r = 0

if right > left:
    print(right - left + 1)
else:
    print(0)
