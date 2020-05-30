class Solution:
    def toLowerCase(self, s: str) -> str:

        s = list(s)
        for i, ele in enumerate(s):
            if ord(ele) >= 65 and ord(ele) <= 90:
                s[i] = chr(ord(ele) + 32)

        return ''.join(s)