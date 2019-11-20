words = [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]

l = []
for ele in words:
    l.append(len(ele))
n = len(words)
m = max(l)

d = {}
record = []
for j in range(m):
    cur  = []
    for i in range(n):
        if j < l[i]:
            if cur and words[i][j] == cur[-1]:
                continue
            cur.append(words[i][j])
    record.append(cur)

for ele in record:
    for i in range(len(ele)):
        if ele[i] not in d:
            d[ele[i]] = set()
            hold = set(ele[i + 1:])
            if ele[i] in hold:
                pass
            else:
                d[ele[i]] = d[ele[i]] | hold

print(d)


