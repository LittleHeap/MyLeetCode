heights = [2, 1, 5, 6, 2, 3]

n = len(heights)
ans = 0
for i in range(n):
    h = heights[i]
    ans = max(ans, h)
    for j in range(i + 1, n):
        h = min(h, heights[j])
        ans = max(ans, h * (j -i + 1))

print(ans)
