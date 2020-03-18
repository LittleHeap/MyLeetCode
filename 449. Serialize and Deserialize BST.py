# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        res = []

        def inorder(node):
            if not node:
                return
            else:
                res.append(node.val)
                inorder(node.left)
                inorder(node.right)

        inorder(root)
        ans = ''
        for ele in res:
            ans += str(ele) + '#'
        ans = ans[:-1]
        return ans

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = data.split('#')

        if not data or data[0] == '':
            return None

        data = list(map(int, data))

        def reinorder(l):
            if not l:
                return None
            node = TreeNode(l[0])
            index = len(l)
            for i in range(len(l)):
                if l[i] > l[0]:
                    index = i
                    break
            node.left = reinorder(l[1:index])
            node.right = reinorder(l[index:])
            return node

        return reinorder(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))