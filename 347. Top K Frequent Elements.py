nums = [1, 1, 1, 2, 2, 3]
k = 2


save = {}

for ele in nums:
    save[ele] = save.get(ele, 0) + 1

temp = sorted(save.items(), key = lambda a: a[1], reverse=True )

res = []
for i in range(k):
    res.append(temp[i][0])

print(res)