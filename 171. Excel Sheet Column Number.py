class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        i = 0
        for index in range(len(s) - 1, -1, -1):
            ans += (ord(s[index]) - 64) * (26 ** i)
            i += 1

        return ans