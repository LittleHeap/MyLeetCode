class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        l = [0]
        done = set()

        def pre(node):
            if True in done:
                return
            if node.left:
                pre(node.left)
                if True in done:
                    return
            res.append(node.val)
            l[0] += 1
            if l[0] == k:
                done.add(True)
                return
            if node.right:
                pre(node.right)
            return

        pre(root)
        return res[-1]
