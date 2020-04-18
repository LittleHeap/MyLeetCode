class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        d = {}

        for num2 in nums2:
            while stack and stack[-1] < num2:
                d[stack.pop()] = num2
            stack.append(num2)

        res = []
        for num1 in nums1:
            res.append(d.get(num1, -1))

        return res