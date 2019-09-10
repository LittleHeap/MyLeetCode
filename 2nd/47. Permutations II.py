import copy


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        save = set()

        def deep(cur, l):
            if not l:
                res.append(cur)
                return
            for i in range(len(l)):
                newcur = copy.deepcopy(cur)
                newl = copy.deepcopy(l)
                newcur.append(l[i])
                newl.pop(i)
                if tuple(newcur) not in save:
                    save.add(tuple(newcur))
                    deep(newcur, newl)

        deep([], nums)
        return res