import copy


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        l = len(words[0])
        se = set(words)
        r = set()
        d = {}
        all = len(words)
        for i in range(all):
            d[words[i]] = d.get(words[i], 0) + 1
            r.add(words[i])

        i = 0
        n = len(s)
        if all * l > n:
            return []
        res = []
        while i < n - l + 1:
            start = s[i: i + l]
            if start in d:
                curd = copy.deepcopy(d)
                curi = i
                curall = all
                while s[curi: curi + l] in se and curd.get(s[curi: curi + l]) > 0:
                    curd[s[curi: curi + l]] -= 1
                    curi += l
                    curall -= 1
                if curall == 0:
                    res.append(i)
                i += 1
            else:
                i += 1
        return res
