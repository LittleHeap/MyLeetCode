height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

maxheight = max(height)
n = len(height)

res = 0
for i in range(1, n - 1):
    if i == 1 or i >= rindex:
        rh = max(height[i + 1:])
        rindex = height[i + 1:].index(rh)
    lh = height[i - 1]
    h = min(lh, rh)
    if h - height[i] > 0:
        res += h - height[i]
        height[i] = h

print(res)
