import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def deep(cur, l):
            if not l:
                res.append(cur)
                return
            for i in range(len(l)):
                newcur = copy.deepcopy(cur)
                newl = copy.deepcopy(l)
                newcur.append(l[i])
                newl.pop(i)
                deep(newcur, newl)

        deep([], nums)
        return res
