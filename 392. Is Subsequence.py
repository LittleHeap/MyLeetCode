class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return 1

        index = 0
        n = len(s)

        for ele in t:
            if ele == s[index]:
                index += 1
            if index == n:
                return 1

        return 0