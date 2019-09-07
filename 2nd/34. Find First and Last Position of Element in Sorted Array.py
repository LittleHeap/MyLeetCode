class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1

        if l == r:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        l, r = mid, mid
        if nums[mid] == target:

            while l - 1 >= 0:
                if nums[l - 1] == target:
                    l -= 1
                else:
                    break
            while r + 1 < len(nums):
                if nums[r + 1] == target:
                    r += 1
                else:
                    break

            return ([l, r])
        else:
            return ([-1, -1])
