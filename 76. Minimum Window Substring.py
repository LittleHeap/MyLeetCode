class Solution:
    def minWindow(self, s: str, t: str) -> str:

        d = {}
        for i in range(len(t)):
            d[t[i]] = d.get(t[i], 0) + 1

        n = len(t)

        curchar = []
        curindex = []

        ans = float('inf')
        res = ''
        for i in range(len(s)):
            if s[i] in d:
                if d.get(s[i]) > 0:
                    curchar.append(s[i])
                    curindex.append(i)
                    d[s[i]] = d.get(s[i]) - 1
                else:
                    index = curchar.index(s[i])
                    curchar.pop(index)
                    curindex.pop(index)
                    curchar.append(s[i])
                    curindex.append(i)
            if len(curchar) == n:
                if curindex[-1] - curindex[0] + 1 < ans:
                    res = s[curindex[0]: curindex[-1] + 1]
                    ans = len(res)

        if len(curchar) != n:
            return ''
        else:
            return res
