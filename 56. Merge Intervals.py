intervals = [[1,4],[4,5]]

intervals.sort()

print(intervals)

res = []
res.append(intervals[0])

for i, ele in enumerate(intervals):
    print(res)
    if i == 0:
        continue
    else:
        if ele[0] >= res[-1][0] and ele[0] <= res[-1][1]:
            if ele[1] <= res[-1][1]:
                continue
            else:
                res[-1][1] = ele[1]
        else:
            res.append(ele)

print(res)
