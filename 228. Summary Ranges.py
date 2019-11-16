class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        n = len(nums)
        i = 0
        while i < n:
            left = i
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if i == left:
                res.append(str(nums[left]))
                i += 1
                continue
            else:
                res.append(str(nums[left]) + '->' + str(nums[i]))
                i += 1
        return res