words = ["area", "lead", "wall", "lady", "ball"]

n = len(words)

l = len(words[0])

hold = [{} for _ in range(l)]

for i, word in enumerate(words):
    for index, char in enumerate(list(word)):
        if char not in hold[index]:
            hold[index][char] = set()
        hold[index][char].add(i)

print(hold)

ans = []


def dfs(cur):
    index = len(cur)
    if index == l:
        ans.append(cur)
        return
    res = set([i for i in range(n)])
    for i in range(index):
        if cur[i][index] in hold[i]:
            res = res & hold[i][cur[i][index]]
        else:
            return
    for j in res:
        newcur = cur.copy()
        newcur.append(words[j])
        dfs(newcur)


for i in range(n):
    dfs([words[i]])

print(ans)
