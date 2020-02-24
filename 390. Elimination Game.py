n = 40

l = [i + 1 for i in range(n)]

flag = 1
while len(l) > 1:
    print(l)
    cur = []
    if flag:
        for i in range(1, len(l), 2):
            cur.append(l[i])
        flag = 0
    else:
        for i in range(len(l) - 2, -1, -2):
            cur.insert(0, l[i])
        flag = 1
    l = cur

print(l)
