intervals = [[1, 4], [0, 1]]

res = []
n = 0

for i in range(len(intervals)):
    print(res)
    if i == 0:
        res.append(intervals[i][0])
        res.append(intervals[i][1])
        n += 2
    else:
        l = n
        while l - 1 >= 0 and res[l - 1] >= intervals[i][0]:
            l -= 1
        res.insert(l, intervals[i][0])
        n += 1

        r = n
        while r - 1 >= 0 and res[r - 1] > intervals[i][1]:
            r -= 1
        res.insert(r, intervals[i][1])
        n += 1

        print(res)

        mid = r - l - 1
        if mid > 0 and mid % 2 == 0:
            for _ in range(l + 1, r):
                res.pop(l + 1)
                n -= 1
            if l != 0 and r != n - 1:
                res.pop(l)
                res.pop(l)
                n -= 2
        else:
            for _ in range(l, r):
                res.pop(l)
                n -= 1

print(res)
