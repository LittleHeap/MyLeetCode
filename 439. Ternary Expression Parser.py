class Solution:
    def parseTernary(self, expression: str) -> str:

        s = []
        for i in expression[::-1]:
            if s and s[-1] == '?':
                if i == 'T':
                    s[-4:] = s[-2]
                else:
                    s[-4:] = s[-4]
            else:
                s.append(i)

        return s[0]