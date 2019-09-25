nums =[121,12]

d = {}
for ele in nums:
    head = int(str(ele)[0])
    if head not in d:
        d[head] = []
    d[head].append(ele)

res = ''
d = sorted(d.items(), key=lambda x: x[0], reverse=True)
for item in d:
    head = item[0]
    cur = item[1]
    l = 0
    for num in cur:
        l = max(l, len(str(num)))
    another = []
    for i, num in enumerate(cur):
        num = list(str(num))
        while len(num) < l:
            num.append(str(head))
        another.append((i, int(''.join(num))))
    another = sorted(another, key=lambda x: x[1], reverse=True)
    for ele in another:
        res += str(cur[ele[0]])
    print(another)

print(res)