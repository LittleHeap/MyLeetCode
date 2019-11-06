nums = [3,30,34,5,9]
n = 0
for ele in nums:
    n = max(len(str(ele)), n)

d = {}
for ele in nums:
    s = str(ele)
    m = len(s)
    head = int(s[-1])
    for _ in range(n - m):
        s += str(head)
    s = int(s)
    d[ele] = s

hold = sorted(d.items(), key=lambda x: x[1], reverse=True)

res = ''
for ele in hold:
    res += str(ele[0])

print(res)
