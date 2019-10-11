class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        def deep(cur, l):
            if not l:
                res.append(cur)
                return
            for i in range(len(l)):
                newcur = cur.copy()
                newl = l.copy()
                if i == 0:
                    newcur.append(newl[i])
                    newl.pop(i)
                    deep(newcur, newl)
                else:
                    if l[i] == l[i - 1]:
                        continue
                    else:
                        newcur.append(newl[i])
                        newl.pop(i)
                        deep(newcur, newl)

        deep([], nums)
        return res
