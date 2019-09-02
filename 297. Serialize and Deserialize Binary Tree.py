# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def deep(node, string):
            if node is None:
                string = string + 'None' + ','
                return string
            else:
                string = string + str(node.val) + ','
                string = deep(node.left, string)
                string = deep(node.right, string)
                return string

        return deep(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rdeep(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            else:
                node = TreeNode(l.pop(0))
                node.left = rdeep(l)
                node.right = rdeep(l)
            return node

        l = data.split(',')
        return rdeep(l)
