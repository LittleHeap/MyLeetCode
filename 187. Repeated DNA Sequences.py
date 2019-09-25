class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        l = 0
        r = 10
        n = len(s)
        if n < 10:
            return []
        d = set()
        res = []
        while r <= n:
            if s[l:r] in d:
                if s[l:r] not in res:
                    res.append(s[l:r])
                l += 1
                r += 1
            else:
                d.add(s[l: r])
                l += 1
                r += 1

        return res
