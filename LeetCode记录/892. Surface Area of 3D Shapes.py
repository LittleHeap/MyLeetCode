grid = [[1, 0], [0, 2]]

n = len(grid)
ans = 0
for i, row in enumerate(grid):
    for j, cur in enumerate(row):
        if cur != 0:
            ans = ans + 2
            if i - 1 == -1:
                ans = ans + cur
            else:
                if grid[i - 1][j] < cur:
                    ans = ans + cur - grid[i - 1][j]
            if j - 1 == -1:
                ans = ans + cur
            else:
                if grid[i][j - 1] < cur:
                    ans = ans + cur - grid[i][j - 1]
            if i + 1 < n:
                if grid[i + 1][j] < cur:
                    ans = ans + cur - grid[i + 1][j]
            else:
                ans = ans + cur
            if j + 1 < n:
                if grid[i][j + 1] < cur:
                    ans = ans + cur - grid[i][j + 1]
            else:
                ans = ans + cur

print(ans)
