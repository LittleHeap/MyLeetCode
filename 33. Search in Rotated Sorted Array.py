class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[l] <= nums[mid]:
                    if target >= nums[l] and target <= nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[l] > nums[mid]:
                    if target >= nums[mid] and target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
        if nums[mid] == target:
            return mid
        if l >= r:
            return -1
