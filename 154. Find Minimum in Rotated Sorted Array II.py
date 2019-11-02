class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = [float('inf')]

        def deep(l):
            if not l:
                return
            if len(l) <= 2:
                res[0] = min(res[0], min(l))
                return
            mid = len(l) // 2
            if l[0] < l[mid]:
                res[0] = min(res[0], l[0])
                deep(l[mid + 1:])
            elif l[mid + 1] < l[-1]:
                res[0] = min(res[0], l[mid + 1])
                deep(l[:mid + 1])
            else:
                deep(l[mid + 1:])
                deep(l[:mid + 1])

        deep(nums)
        return res[0]