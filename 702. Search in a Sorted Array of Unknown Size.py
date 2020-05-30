# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l = 1
        while reader.get(l) < target:
            l = l << 1
        r = l >> 1
        while r <= l:
            mid = (r + l) >> 1
            if reader.get(mid) < target:
                r = mid + 1
            elif reader.get(mid) > target:
                l = mid - 1
            else:
                return mid

        return -1