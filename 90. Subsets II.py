class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()

        res = []

        def deep(cur, l):
            res.append(cur)
            if not l:
                return
            for i in range(len(l)):
                if i > 0 and l[i] == l[i - 1]:
                    continue
                else:
                    newcur = copy.deepcopy(cur)
                    newl = copy.deepcopy(l)
                    newcur.append(newl[i])
                    newl = newl[i + 1:]
                    deep(newcur, newl)

        deep([], nums)
        return (res)
