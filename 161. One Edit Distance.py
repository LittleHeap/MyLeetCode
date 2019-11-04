class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)

        m = len(s)
        n = len(t)

        if m == 0 and n == 0:
            return False

        i = 0
        while i < min(m, n):
            if s[i] != t[i]:
                break
            else:
                i += 1

        if i == m and i == n:
            return False

        if s[i + 1:] == t[i + 1:]:
            return True
        elif s[i + 1:] == t[i:]:
            return True
        elif s[i:] == t[i + 1:]:
            return True
        else:
            return False
