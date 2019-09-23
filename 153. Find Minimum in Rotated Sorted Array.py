class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = [float('inf')]

        def bi(l, r):
            if r - l <= 1:
                res[0] = min(res[0], nums[l])
                return
            mid = (l + r) // 2
            if nums[l] <= nums[mid - 1]:
                res[0] = min(res[0], nums[l])
                bi(mid, r)
            else:
                res[0] = min(res[0], nums[mid])
                bi(l, mid)

        bi(0, len(nums))

        return res[0]
