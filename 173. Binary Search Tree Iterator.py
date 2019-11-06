# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.l = []

        def mid(node):
            if node is None:
                return
            mid(node.left)
            self.l.append(node.val)
            mid(node.right)

        mid(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.l.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.l:
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()