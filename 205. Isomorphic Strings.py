class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        n = len(s)
        m = len(t)
        if m != n:
            return False
        for i in range(n):
            if s[i] not in d:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        return True
