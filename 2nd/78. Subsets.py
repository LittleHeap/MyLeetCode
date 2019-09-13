import copy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def deep(l, cur):
            for i in range(len(l)):
                newcur = copy.deepcopy(cur)
                newcur.append(l[i])
                res.append(newcur)
                newl = copy.deepcopy(l)
                newl = newl[i + 1:]
                deep(newl, newcur)

        deep(nums, [])
        return res
