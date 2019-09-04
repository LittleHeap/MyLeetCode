class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        res = ''
        s = list(s)
        n = len(s)

        if n == 0:
            return ''
        else:
            ans = 1
            res = s[0]

        for i in range(n):
            cur = 1
            kuo = 1
            while i + kuo < n and i - kuo >= 0:
                if s[i - kuo] == s[i + kuo]:
                    cur = cur + 2
                    if cur > ans:
                        ans = cur
                        res = s[i - kuo: i + kuo + 1]
                    kuo += 1
                else:
                    break
            cur = 0
            l = 1
            r = 0
            while i - r >= 0 and i + l < n:
                if s[i - r] == s[i + l]:
                    cur = cur + 2
                    if cur > ans:
                        ans = cur
                        res = s[i - r: i + l + 1]
                    r += 1
                    l += 1
                else:
                    break
        return ''.join(res)
