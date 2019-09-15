import copy
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]

        res = []
        def deep(cur, l):
            if len(cur) + len(l) < k:
                return
            if len(cur) == k:
                res.append(cur)
                return
            if not l:
                return
            for i in range(len(l)):
                newcur = copy.deepcopy(cur)
                newl = copy.deepcopy(l)
                newcur.append(l[i])
                newl = newl[i + 1:]
                deep(newcur, newl)

        deep([], nums)
        return (res)