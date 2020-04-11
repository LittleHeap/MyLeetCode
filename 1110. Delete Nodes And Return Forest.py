# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        if not root:
            return []

        to_delete = set(to_delete)

        hold = []

        def deep(node, gen):
            if not node:
                return None
            if node.val in to_delete:
                deep(node.left, 1)
                deep(node.right, 1)
                return None
            else:
                node.left = deep(node.left, 0)
                node.right = deep(node.right, 0)
                if gen:
                    hold.append(node)
                    return None
                else:
                    return node

        deep(root, 1)

        res = sorted(hold, key=lambda x: x.val)
        return res


