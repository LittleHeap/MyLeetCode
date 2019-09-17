class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l = len(nums) - 1
        r = 0

        while r <= l:
            mid = (l + r) // 2
            rmid = mid
            lmid = mid
            while rmid - 1 >= r and nums[rmid] == nums[rmid - 1]:
                rmid -= 1
            while lmid + 1 <= l and nums[lmid] == nums[lmid + 1]:
                lmid += 1
            if rmid - 1 >= r:
                rmid -= 1
            if lmid + 1 <= l:
                lmid += 1
            if target == nums[mid] or target == nums[l] or target == nums[r] or target == nums[rmid] or target == nums[
                lmid]:
                return True
            if nums[r] <= nums[rmid]:
                if target > nums[r] and target < nums[rmid]:
                    l = rmid - 1
                else:
                    r = lmid + 1
            else:
                if target > nums[mid] and target < nums[l]:
                    r = lmid + 1
                else:
                    l = rmid - 1
        return False
