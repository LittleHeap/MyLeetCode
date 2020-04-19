class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        d = {}

        def deep(c1, c2):
            if c1 == c2:
                return True
            if (c1, c2) in d:
                return d[(c1, c2)]
            for i in range(1, len(c1)):
                if (deep(c1[:i], c2[:i]) and deep(c1[i:], c2[i:])):
                    d[(c1, c2)] = True
                    return True
                if (deep(c1[:i], c2[len(c2) - i:]) and deep(c1[i:], c2[:len(c2) - i])):
                    d[(c1, c2)] = True
                    return True
                d[(c1, c2)] = False

        return deep(s1, s2)
