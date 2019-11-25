s = '++++'

res = 0

n = len(s)

i = 0
while i < n:
    print(i)
    if s[i] == '+':
        l = 1
        while i + 1 < n and s[i + 1] == '+':
            i += 1
            l += 1
        if l % 2 == 1:
            res += 2
        else:
            res += 1
    else:
        i += 1

