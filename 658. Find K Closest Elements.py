class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        index = bisect.bisect_left(arr, x)

        l, r = index - 1, index

        while r - l <= k:
            if l == -1:
                r += 1
            elif r == len(arr):
                l -= 1
            else:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    l -= 1
                else:
                    r += 1

        return arr[l + 1:r]