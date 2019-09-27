mapping = [3, 5, 4, 6, 2, 7, 9, 8, 0, 1]
nums = ['990', '332', '32']

save = {}
num = {}

for i in range(10):
    num[mapping[i]] = i

for ele in nums:
    cur = []
    for i in range(len(ele)):
        digit = int(ele[i])
        cur.append(str(num.get(digit)))
    cur = ''.join(cur)
    p = int(cur)
    if p not in save:
        save[p] = [ele]
    else:
        save[p].append(ele)
    cur = save.get(p, [])


save = sorted(save.items(), key=lambda x:x[0])
res = []
for ele in save:
    res.extend(ele[1])

print(res)

