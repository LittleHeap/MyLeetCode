s = "ADOBECODEBANC"
t = "ABC"

d = {}
m = len(s)
n = len(t)

for i in range(n):
    d[t[i]] = d.get(t[i], 0) + 1

l = float('inf')
res = ''

c = []
num = []
for i in range(m):
    if s[i] in d:
        if d[s[i]] > 0:
            c.append(s[i])
            num.append(i)
            d[s[i]] -= 1
        else:
            index = c.index(s[i])
            c.pop(index)
            num.pop(index)
            c.append(s[i])
            num.append(i)
        if len(c) == n:
            if num[-1] - num[0] + 1 < l:
                res = s[num[0]: num[-1] + 1]
                l = len(res)

print(res)