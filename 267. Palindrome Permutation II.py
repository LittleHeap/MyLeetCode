class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        d = set()
        hold = []

        if len(set(list(s))) == 1:
            return [s]

        for ele in s:
            if ele in d:
                d.remove(ele)
                hold.append(ele)
            else:
                d.add(ele)

        if len(d) > 1:
            return []

        res = []
        fin = set()

        def deep(l, cur):
            if not l:
                if ''.join(cur) in fin:
                    return
                else:
                    fin.add(''.join(cur))
                if len(d) == 1:
                    last = cur.copy()
                    last.reverse()
                    ans = ''.join(cur) + list(d)[0] + ''.join(last)
                    res.append(ans)
                else:
                    last = cur.copy()
                    last.reverse()
                    ans = ''.join(cur) + ''.join(last)
                    res.append(ans)
                return
            else:
                for i in range(len(l)):
                    newcur = cur.copy()
                    newcur.append(l[i])
                    newl = l.copy()
                    newl.pop(i)
                    deep(newl, newcur)

        deep(hold, [])
        return res