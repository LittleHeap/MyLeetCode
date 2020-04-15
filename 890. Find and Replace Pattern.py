class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        res = []
        for word in words:
            d = {}
            done = set()
            for i in range(len(pattern)):
                if word[i] in d:
                    if d[word[i]] != pattern[i]:
                        break
                else:
                    if pattern[i] not in done:
                        d[word[i]] = pattern[i]
                        done.add(pattern[i])
                    else:
                        break
                if i == len(pattern) - 1:
                    res.append(word)

        return res