class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        s = list(s)

        for i in range(0, len(s), 2 * k):
            if i + 2 * k <= len(s) or len(s) > i + k:
                cur = s[i:i + k].copy()
                for j in range(i, i + k, 1):
                    s[j] = cur[-j + i - 1]
            else:
                cur = s[i:].copy()
                for j in range(i, len(s)):
                    s[j] = cur[-j + i - 1]

        return ''.join(s)