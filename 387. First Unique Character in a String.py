class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = []
        d = {}
        h = set()

        for i in range(len(s)):
            if s[i] in h:
                continue
            if s[i] not in d:
                d[s[i]] = i
            else:
                d.pop(s[i])
                h.add(s[i])

        ans = float('inf')
        if not d:
            return -1

        for ele in d.items():
            ans = min(ans, ele[1])

        return ans
