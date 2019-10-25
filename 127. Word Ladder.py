beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

wordList = set(wordList)
# if endWord not in wordList:
#     return 0
beginWord = list(beginWord)
endWord = list(endWord)

ans = 0
n = len(beginWord)
while beginWord != endWord:
    print(beginWord)
    temp = beginWord.copy()
    for i in range(n):
        if beginWord[i] != endWord[i]:
            beginWord[i] = endWord[i]
            if ''.join(beginWord) in wordList:
                ans += 1
                break
            else:
                beginWord = temp.copy()
    if beginWord == temp:
        break

print(ans)