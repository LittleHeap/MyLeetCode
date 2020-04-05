class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:

        res = 0

        d = collections.Counter(words)

        c = defaultdict(list)
        for i, char in enumerate(S):
            c[char].append(i)

        done = set()

        for word in d:
            n = len(word)
            i = 0
            pre = -1
            while i < n:
                if word[i] not in c:
                    break
                else:
                    index = bisect.bisect_right(c[word[i]], pre)
                    if index != len(c[word[i]]):
                        pre = c[word[i]][index]
                        i += 1
                    else:
                        break
            if i == n:
                res += d[word]

        return res