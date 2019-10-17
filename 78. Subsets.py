class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        res.append([])

        def deep(l, cur):
            if not l:
                return
            for i in range(len(l)):
                newcur = cur.copy()
                newcur.append(l[i])
                res.append(newcur)
                newl = l.copy()
                newl = newl[i + 1:]
                deep(newl, newcur)

        deep(nums, [])
        return res