import copy

s = "barfoothefoobarman"
words = ["foo","bar"]
n = len(words[0])
m = len(words)

hold = set()


def deep(cur, l):
    if not l:
        hold.add(cur)
        return
    for i in range(len(l)):
        newl = copy.deepcopy(l)
        newcur = copy.deepcopy(cur)
        newcur += newl.pop(i)
        deep(newcur, newl)


deep('', words)

res = []
for i in range(len(s) - n * m  + 1):
    if s[i:i + n * m] in hold:
        res.append(i)

print(res)
