class Solution:
    def reverseWords(self, s: str) -> str:

        s = list(s)

        res = []
        while s:
            while s and s[0] == ' ':
                s.pop(0)
            if not s:
                break
            cur = []
            while s and s[0] != ' ':
                cur.append(s.pop(0))
            if not s:
                res.append(''.join(cur))
                break
            res.append(''.join(cur))

        res.reverse()
        ans = ''
        for ele in res:
            ans += ele + ' '

        ans = ans[:-1]
        return ans