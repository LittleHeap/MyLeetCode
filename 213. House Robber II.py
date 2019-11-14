class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 2:
            return max(nums)

        nums1 = nums.copy()[:-1]
        nums2 = nums.copy()[1:]

        for i in range(2, n - 1):
            nums1[i] += max(nums1[:i - 1])
            nums2[i] += max(nums2[:i - 1])

        nums1.extend(nums2)
        return max(nums1)
