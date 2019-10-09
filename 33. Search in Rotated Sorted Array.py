class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)

        def bi(l, r):
            if l > r or l >= n or r < 0:
                return -1
            index = (l + r + 1) // 2
            if nums[index] == target:
                return index
            elif l == r and target != nums[l]:
                return -1
            else:
                if nums[l] <= nums[index - 1]:
                    if target <= nums[index - 1] and target >= nums[l]:
                        return bi(l, index - 1)
                    else:
                        return bi(index + 1, r)
                else:
                    if target >= nums[index + 1] and target <= nums[r]:
                        return bi(index + 1, r)
                    else:
                        return bi(l, index - 1)

        return bi(0, len(nums) - 1)
