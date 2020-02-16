class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        for ele in nums1:
            d1[ele] = d1.get(ele, 0) + 1

        d2 = {}
        for ele in nums2:
            d2[ele] = d2.get(ele, 0) + 1

        res = []
        for k1 in d1:
            if k1 in d2:
                res.extend([k1 for _ in range(min(d1[k1], d2[k1]))])

        return res