class WordDistance:

    def __init__(self, words: List[str]):
        self.w = words
        self.save = {}
        self.d = {}
        for i in range(len(words)):
            if words[i] in self.d:
                self.d[words[i]].append(i)
            else:
                self.d[words[i]] = [i]

    def shortest(self, word1: str, word2: str) -> int:
        if (word1, word2) in self.save:
            return self.save[(word1, word2)]

        w1 = self.d[word1]
        w2 = self.d[word2]

        n1 = len(w1)
        n2 = len(w2)
        i = 0
        j = 0
        dis = float('inf')
        while i < n1 and j < n2:
            dis = min(dis, abs(w1[i] - w2[j]))
            if w1[i] == w2[j]:
                break
            elif w1[i] < w2[j]:
                i += 1
            else:
                j += 1

        self.save[(word1, word2)] = dis
        self.save[(word2, word1)] = dis
        return dis

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)