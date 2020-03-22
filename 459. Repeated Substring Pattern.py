class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        n = len(s)
        for i in range(n - 1):
            if n % (i + 1) == 0:
                times = n // (i + 1)
                if s[:i + 1] * times == s:
                    return True

        return False