matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 13

res = []

for i in range(len(matrix)):
    res.extend(matrix[i])

l = 0
r = len(res) - 1
ans = set()

while l <= r:
    mid = (l + r) // 2
    if res[mid] == target:
        ans.add(True)
        break
    elif res[mid] > target:
        r = mid - 1
    else:
        l = mid + 1

print(True in ans)