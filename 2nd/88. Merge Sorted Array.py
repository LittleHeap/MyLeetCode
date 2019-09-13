class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = len(nums1)
        i1 = 0
        n2 = len(nums2)
        i2 = 0
        while i2 < n and i1 - i2 < m:
            if nums2[i2] <= nums1[i1]:
                nums1.insert(i1, nums2[i2])
                i2 += 1
            else:
                i1 += 1
                if nums1[i1] < nums1[i1 - 1]:
                    break
        while i2 < n2:
            nums1[i1] = nums2[i2]
            i1 += 1
            i2 += 1
        for _ in range(len(nums1) - n1):
            nums1.pop()
