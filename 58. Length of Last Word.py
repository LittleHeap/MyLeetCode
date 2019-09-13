class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0

        n = len(s)
        if n == 0:
            return 0

        res = 0
        pre = 0
        while i < n:
            if s[i] != ' ':
                res += 1
                i += 1
            else:
                pre = res
                res = 0
                while i < n and s[i] == ' ':
                    i += 1
        if s[i - 1] == " ":
            return pre
        else:
            return res