a = "1111"
b = "1111"

a = list(a)
b = list(b)

m = len(a)
n = len(b)

for i in range(m):
    if a[i] == '1':
        a[i] = 1
    else:
        a[i] = 0

for j in range(n):
    if b[j] == '1':
        b[j] = 1
    else:
        b[j] = 0

if m > n:
    for _ in range(m - n):
        b.insert(0, 0)
else:
    for _ in range(n - m):
        a.insert(0, 0)

flag = 0
for i in range(max(m, n) - 1, -1 ,-1):
    a[i] += b[i] + flag
    if a[i] >= 2:
        a[i] %= 2
        flag = 1
    else:
        flag = 0

if flag:
    a.insert(0, 1)

res = ""
for ele in a:
    res += str(ele)

print(res)