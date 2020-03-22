class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:

        size = len(p)

        hold = [0] * 26

        l = 0

        for i in range(len(p)):
            index = ord(p[i]) - 97
            if i > 0 and ord(p[i - 1]) - 97 == (index - 1) % 26:
                l += 1
            else:
                l = 1
            hold[index] = max(hold[index], l)

        return sum(hold)