s = "bcabc"


n = len(s)

cur = []
have = set()

for i in range(n):
    if s[i] not in have:
        have.add(s[i])
        cur.append(s[i])
    else:
        if cur[-1] == s[i]:
            continue
        else:
            index = cur.index(s[i])
            if cur[index + 1] < s[i]:
                cur.pop(index)
                cur.append(s[i])

print(cur)