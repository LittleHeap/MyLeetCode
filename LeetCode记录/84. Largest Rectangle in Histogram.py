heights = [2, 1, 5, 6, 2, 3]

ans = 0
small = float('inf')
curheight = 0
for i in range(len(heights)):
    small = min(small, heights[i])
    ans = max(ans, heights[i])
    curheight = heights[i]
    for j in range(i - 1, -1, -1):
        curheight = min(curheight, heights[j])
        if curheight == small:
            ans = max(ans, (i + 1) * small)
            break
        elif curheight < small:
            small = curheight
            ans = max(ans, (i + 1) * small)
            break
        ans = max(ans, (i - j + 1) * curheight)

print(ans)
