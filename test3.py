s = 'aabaa'

n = len(s)
hold = set()
res = 0
for i in range(n):
    if s[i] not in hold:
        res += 1
        hold.add(s[i])
    l = i
    r = i
    print(i)
    while l - 1 >= 0 and r + 1 < n and s[l - 1] == s[r + 1]:
        l -= 1
        r += 1
        if s[l: r + 1] not in hold:
            hold.add(s[l:r + 1])
            res += 1
    l = i + 1
    r = i
    while l - 1 >= 0 and r + 1 < n and s[l - 1] == s[r + 1]:
        l -= 1
        r += 1
        if s[l: r + 1] not in hold:
            hold.add(s[l:r + 1])
            res += 1

print(res)
