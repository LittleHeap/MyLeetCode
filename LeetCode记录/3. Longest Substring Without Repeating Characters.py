class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        have = set()
        l = 0
        r = 1
        n = len(s)
        have.add(s[l])
        res = 1
        while r < n:
            if s[r] not in have:
                have.add(s[r])
                r += 1
            else:
                res = max(res, len(have))
                while s[l] != s[r]:
                    have.remove(s[l])
                    l += 1
                l += 1
                r += 1
        res = max(res, len(have))
        return res
