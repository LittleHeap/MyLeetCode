class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif l == r:
                if nums[l] < target:
                    return l + 1
                else:
                    return l
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if r == -1:
            return 0
        else:
            return l