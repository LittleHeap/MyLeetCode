n = 6

res = []
def deep(l, level):
    if level == n:
        res.append(l)
        return
    pre = l[0]
    i = 0
    count = 1
    new = []
    while i + 1 < len(l):
        if l[i + 1] == pre:
            count += 1
        else:
            new.append(count)
            new.append(pre)
            count = 1
            pre = l[i + 1]
        i += 1
    new.append(count)
    new.append(pre)
    deep(new, level + 1)
    return

deep([1], 1)
print(res)

print(''.join(res))