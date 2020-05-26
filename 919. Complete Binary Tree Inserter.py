# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.l = []
        q = [root]
        while q:
            cur = q.pop(0)
            self.l.append(cur)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    def insert(self, v: int) -> int:
        self.l.append(TreeNode(v))
        if len(self.l) > 1:
            if len(self.l) % 2 == 0:
                self.l[len(self.l) // 2 - 1].left = self.l[-1]
                return self.l[len(self.l) // 2 - 1].val
            else:
                self.l[(len(self.l) - 1) // 2 - 1].right = self.l[-1]
                return self.l[(len(self.l) - 1) // 2 - 1].val

    def get_root(self) -> TreeNode:
        return (self.l[0] if self.l else None)

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()