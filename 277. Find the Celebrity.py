# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = [[] for _ in range(n)]

        for i in range(n):
            flag = 0
            for up in range(i - 1, -1, -1):
                if knows(up, i) == 0:
                    flag = 1
                    break
            if flag == 1:
                continue
            for down in range(i + 1, n):
                if knows(down, i) == 0:
                    flag = 1
                    break
            if flag == 1:
                continue
            for left in range(i - 1, -1, -1):
                if knows(i, left) == 1:
                    flag = 1
                    break
            if flag == 1:
                continue
            for right in range(i + 1, n):
                if knows(i, right) == 1:
                    flag = 1
                    break
            if flag == 1:
                continue
            return i
        return -1