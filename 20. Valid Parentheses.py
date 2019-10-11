class Solution:
    def isValid(self, s: str) -> bool:

        l = ['(', '[', '{']
        r = [')', ']', '}']

        cur = []
        for i in range(len(s)):
            if s[i] in l:
                cur.append(s[i])
            else:
                if not cur:
                    return False
                last = cur.pop()
                if last in l:
                    if l.index(last) != r.index(s[i]):
                        return False
                else:
                    return False
        return not cur