class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}

        for i in range(len(s)):
            if s[i] == t[i]:
                if s[i] not in d:
                    d[s[i]] = t[i]
                else:
                    if d[s[i]] != t[i]:
                        return False
            else:
                if s[i] not in d:
                    if t[i] in d.values():
                        return False
                    d[s[i]] = t[i]
                else:
                    if d[s[i]] != t[i]:
                        return False
        return True
