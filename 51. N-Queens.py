import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = set()
        pie = set()
        na = set()

        res = []
        cur = [['.' for _ in range(n)] for _ in range(n)]

        def deep(i, col, pie, na, cur):
            if i == n:
                res.append(cur)
                return
            for e in range(n):
                if e not in col and e - i not in pie and e + i not in na:
                    newcur = copy.deepcopy(cur)
                    newcur[i][e] = 'Q'
                    newcol = copy.deepcopy(col)
                    newcol.add(e)
                    newpie = copy.deepcopy(pie)
                    newpie.add(e - i)
                    newna = copy.deepcopy(na)
                    newna.add(e + i)
                    deep(i + 1, newcol, newpie, newna, newcur)

        deep(0, col, pie, na, cur)
        ans = []
        for ele in res:
            cur = []
            for i in range(n):
                cur.append(''.join(ele[i]))
            ans.append(cur)
        return ans