class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        hold = set()

        def deep(cur, l):
            if tuple(cur) not in hold:
                res.append(cur)
                hold.add(tuple(cur))
            if not l:
                return
            for i in range(len(l)):
                newcur = cur.copy()
                newcur.append(l[i])
                deep(newcur, l[i + 1:])

        deep([], nums)
        return res
