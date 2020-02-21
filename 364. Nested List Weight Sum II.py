# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        if not nestedList:
            return 0

        depth = [0]
        res = [0]

        def deep(l, d):
            if l.isInteger():
                depth[0] = max(depth[0], d + 1)
            else:
                for ele in l.getList():
                    deep(ele, d + 1)

        for ele in nestedList:
            deep(ele, 0)

        def re(l, d):
            if l.isInteger():
                res[0] += l.getInteger() * d
            else:
                for ele in l.getList():
                    re(ele, d - 1)

        for ele in nestedList:
            re(ele, depth[0])

        return res[0]












