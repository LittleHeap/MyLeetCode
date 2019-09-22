beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

beginWord = list(beginWord)
endWord = list(endWord)

done = set()

ans = [0]
res = set()
def deep(cur):
    if True in res:
        return
    if cur == endWord:
        res.add(True)
        return
    for i in range(len(wordList)):
        s1 = set(list(wordList[i]))
        s2 = set(cur)
        if len(s1 & s2) == 1:
            temp = cur
            cur = wordList[i]
            now = wordList[i]
            wordList.remove(now)
            ans[0] += 1
            deep(cur)
            cur = temp
            wordList.append(now)

deep(beginWord)
print(ans)