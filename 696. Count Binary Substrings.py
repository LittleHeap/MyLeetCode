class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        res = 0

        pre = None
        cur = 0
        start, end = 0, 0
        while end < len(s):
            while end + 1 < len(s) and s[end + 1] == s[end]:
                end += 1
            if pre:
                res += min(pre, end - start + 1)
            pre = end - start + 1
            start, end = end + 1, end + 1

        return res

