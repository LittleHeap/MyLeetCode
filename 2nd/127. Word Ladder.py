beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]

d = {}
n = len(wordList)
hold = set()
target = set(list(beginWord))
l = len(beginWord)


def comp(a, b):
    count = 0
    for i in range(l):
        if a[i] != b[i]:
            count += 1
            if count >= 2:
                return False
    if count == 1:
        return True
    else:
        return False


for i in range(n):
    if comp(wordList[i], beginWord):
        hold.add(wordList[i])
    for j in range(i + 1, n):
        if comp(wordList[i], wordList[j]):
            if wordList[i] in d:
                d[wordList[i]].append(wordList[j])
            else:
                d[wordList[i]] = [wordList[j]]
            if wordList[j] in d:
                d[wordList[j]].append(wordList[i])
            else:
                d[wordList[j]] = [wordList[i]]

done = set()
done.add(endWord)
res = [float('inf')]
find = set()

def deep(cur, level):
    print(cur)
    print(level)
    if 1 in find:
        return
    newcur = []
    for ele in cur:
        have = d[ele]
        for k in have:
            if k in hold:
                res[0] = level + 1
                find.add(1)
                return
            else:
                newcur.append(k)
    deep(newcur, level + 1)

print(hold)
print(d)
deep([endWord], 1)
print(res[0])
