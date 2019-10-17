class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        if not nums:
            return False
        find = [0]

        def deep(l, r):
            if find[0] == 1:
                return
            mid = (l + r) // 2
            if nums[mid] == target or nums[l] == target or nums[r] == target:
                find[0] = 1
            elif l >= r:
                return
            else:
                deep(l + 1, mid - 1)
                deep(mid + 1, r - 1)

        deep(0, len(nums) - 1)
        return find[0] == 1
