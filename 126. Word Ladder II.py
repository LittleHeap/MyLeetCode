class Solution:
    def findLadders(self, begin: str, end: str, wordList: List[str]) -> List[List[str]]:

        wordList = set(wordList)
        res = []
        layer = {}
        layer[begin] = [[begin]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == end:
                    res += [k for k in layer[w]]
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new = w[:i] + c + w[i + 1:]
                            if new in wordList:
                                newlayer[new] += [j + [new] for j in layer[w]]
            if res:
                return res
            else:
                wordList -= set(newlayer.keys())
                layer = newlayer

        return []