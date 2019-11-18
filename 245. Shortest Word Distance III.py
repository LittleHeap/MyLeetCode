class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:

        n = len(words)
        d = {}

        for i in range(n):
            if words[i] in d:
                d[words[i]].append(i)
            else:
                d[words[i]] = [i]

        if word1 == word2:
            ans = float('inf')
            l = d[word1]
            for i in range(1, len(l)):
                ans = min(ans, l[i] - l[i - 1])
            return ans
        else:
            w1 = 0
            w2 = 0
            l1 = d[word1]
            l2 = d[word2]
            n1 = len(l1)
            n2 = len(l2)
            ans = float('inf')
            while w1 < n1 and w2 < n2:
                ans = min(ans, abs(l1[w1] - l2[w2]))
                if ans == 0:
                    break
                elif l1[w1] < l2[w2]:
                    w1 += 1
                else:
                    w2 += 1
            return ans


