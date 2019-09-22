s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

word = []
for i in range(len(wordDict)):
    word.append((wordDict[i], len(wordDict[i])))

word = sorted(word, key=lambda x: x[1])

wordDict = set(wordDict)
n = len(s)

res = []
save = {}


def deep(s, l, cur):
    if l and l[-1] == n:
        ans = ''
        for ele in cur:
            ans += ele + ' '
        ans = ans[:-1]
        res.append(ans)
        return
    if not l:
        for i in range(1, n + 1):
            if s[:i] in wordDict:
                newl = l.copy()
                newl.append(i)
                newcur = cur.copy()
                newcur.append(s[:i])
                deep(s, newl, newcur)
    else:
        for i in range(l[-1] + 1, n + 1):
            if s[l[-1]:i] in wordDict:
                newl = l.copy()
                newl.append(i)
                newcur = cur.copy()
                newcur.append(s[l[-1]:i])
                deep(s, newl, newcur)


deep(s, [], [])
print(res)
