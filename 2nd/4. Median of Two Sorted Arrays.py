class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        num = []
        n1, n2 = None, None
        if nums1:
            n1 = nums1.pop(0)
        if nums2:
            n2 = nums2.pop(0)
        while n1 is not None or n2 is not None:
            if n1 == None:
                num.append(n2)
                num.extend(nums2)
                break
            if n2 == None:
                num.append(n1)
                num.extend(nums1)
                break
            if n1 < n2:
                num.append(n1)
                if nums1:
                    n1 = nums1.pop(0)
                else:
                    n1 = None
            elif n1 > n2:
                num.append(n2)
                if nums2:
                    n2 = nums2.pop(0)
                else:
                    n2 = None
            else:
                num.append(n1)
                if nums1:
                    n1 = nums1.pop(0)
                else:
                    n1 = None
        n = len(num)
        print(num)
        if n % 2 == 0:
            return (num[n // 2] + num[n // 2 - 1]) / 2
        else:
            return num[(n - 1) // 2]