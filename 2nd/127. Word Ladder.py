beginWord = "hit"
endWord = "cog"
wordList = ["hot","cog","dot","dog","hit","lot","log"]

wordList.sort()
print(wordList)
n = len(wordList)
l = len(wordList[0])
start = wordList.index(endWord)
ans = float('inf')


def can(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    count = 0
    for i in range(l):
        if s1[i] != s2[i]:
            count += 1
        if count >= 2:
            return False
    if count == 1:
        return True
    else:
        return False


left = start + 1
res = [endWord]
while left < n:
    if can(wordList[left - 1], wordList[left]):
        res.append(wordList[left])
        if wordList[left] == beginWord:
            break
        else:
            left += 1
    else:
        break
if res[-1] == beginWord:
    ans = min(ans, len(res))
if can(res[-1], beginWord):
    ans = min(ans, len(res) + 1)

right = start - 1
res = [endWord]
while right >= 0:
    if can(wordList[right + 1], wordList[right]):
        res.append(wordList[right])
        if wordList[right] == beginWord:
            break
        else:
            right -= 1
    else:
        break
if res[-1] == beginWord:
    ans = min(ans, len(res))
if can(res[-1], beginWord):
    ans = min(ans, len(res) + 1)

if ans == float('inf'):
    print(0)
else:
    print(ans)
