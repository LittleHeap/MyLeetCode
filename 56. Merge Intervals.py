intervals = [[2,3],[4,6],[5,7],[3,4]]

res = []
for ele in intervals:
    print(res)
    print(ele)
    if len(res) == 0:
        res.append(ele)
        continue
    flag = 0
    ru = 0
    for i in range(len(res)):
        if res[i] == 0:
            continue
        if ele[0] <= res[i][1] and ele[0] >= res[i][0]:
            res[i][1] = max(ele[1], res[i][1])
            ru = 1
            break
        elif ele[1] >= res[i][0] and ele[1] <= res[i][1]:
            res[i][0] = min(ele[0], res[i][0])
            ru = 1
            break
        elif ele[0] < res[i][0] and ele[1] > res[i][1]:
            ru = 1
            if flag:
                res[i] = 0
                continue
            res[i][0] = ele[0]
            res[i][1] = ele[1]
            flag = 1
        elif ele[0] > res[i][0] and ele[1] < res[i][1]:
            ru = 1
            break
    if ru == 0:
        res.append(ele)


while 0 in res:
    res.remove(0)
print(res)
