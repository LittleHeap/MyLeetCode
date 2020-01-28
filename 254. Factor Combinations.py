n = 32

hold = set()
res = []

def deep():
    if len(res) == 0:
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                new = [i, n // i]
                new.sort()
                if tuple(new) not in hold:
                    res.append(new)
                    hold.add(tuple(new))
                    deep()
                else:
                    return
    else:
        target = res[-1][-1]
        origin = res[-1][:-1]
        for i in range(2, target // 2 + 1):
            if target % i == 0:
                new = origin + [i, target // i]
                new.sort()
                if tuple(new) not in hold:
                    res.append(new)
                    hold.add(tuple(new))
                    deep()
                else:
                    return

deep()
print(res)