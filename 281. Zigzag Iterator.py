class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.l = []
        flag = 1
        while v1 and v2:
            if flag == 1:
                self.l.append(v1.pop(0))
                flag = 2
            else:
                self.l.append(v2.pop(0))
                flag = 1
        if v1:
            self.l.extend(v1)
        if v2:
            self.l.extend(v2)

    def next(self):
        """
        :rtype: int
        """
        return self.l.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.l:
            return True
        else:
            return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())