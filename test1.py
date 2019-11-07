n = 72328

n = list(str(n))
l = len(n)

for i in range(0, l, 2):
    if i + 1 < l:
        n[i], n[i + 1] = n[i + 1], n[i]

n = int(''.join(n))
print(n)
