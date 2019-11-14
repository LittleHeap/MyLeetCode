s = "ababbbabbaba"

m = 0
index = 0

n = len(s)
for i in range(n):
    print(index)
    print(m)
    # ji
    l = i - 1
    r = i + 1
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    length = r - l - 2 + 1
    if i - length // 2== 0 and length > m:
        m = length
        index = i
    # ou
    l = i
    r = i + 1
    while l >= 0 and r < n and s[l] == s[r]:
        l -= 1
        r += 1
    length = r - l - 1
    if i - length // 2 + 1 == 0 and length > m:
        m = length
        index = i

print(index)
print(m)
if m % 2 == 1:
    s = s[index:]
    ad = list(s[1:])
    ad.reverse()
    s = ''.join(ad) + s
else:
    ad = list(s[index + m // 2 + 1:])
    ad.reverse()
    s = ''.join(ad) + s

print(s)

