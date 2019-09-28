n = 34522

p = 0
res = 0
n = list(str(n))
for i in range(len(n) - 1, - 1, - 1):
    num = int(n[i])
    if i == len(n) - 1:
        if num >= 5:
            res += 1
            pre = 1
        else:
            pre = 0
        p = 1
    else:
        res += num * (p + pre)
        pre = res
        p += 1


print(res)


