# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:
            mid = (l + r) // 2
            if mid - 1 >= 1 and isBadVersion(mid) == 1 and isBadVersion(mid - 1) == 0:
                return mid
            if mid - 1 == 0 and isBadVersion(mid) == 1:
                return 1
            if isBadVersion(mid) == 0:
                l = mid + 1
            elif isBadVersion(mid) == 1:
                r = mid - 1