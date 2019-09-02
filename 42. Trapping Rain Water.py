height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

h = max(height)
w = len(height)
water = 0
front = 0
back = max(height[2:])
back_index = height[2:].index(back) + 2

for i in range(1, w - 1):
    front = max(front, height[i - 1])
    if i == back_index:
        back = max(height[i + 1:])
        back_index = height[i + 1:].index(back) + i + 1
    if front > height[i] and back > height[i]:
        water = water + min(front, back) - height[i]

print(water)
