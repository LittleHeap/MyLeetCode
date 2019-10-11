class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def deep(l, cur):
            if not l:
                res.append(cur)
                return
            for i in range(len(l)):
                newcur = cur.copy()
                newcur.append(l[i])
                newl = l.copy()
                newl.remove(l[i])
                deep(newl, newcur)

        deep(nums, [])
        return res
