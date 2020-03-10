"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ''
        res = ''

        def deep(node):
            cur = '['
            cur += str(node.val)
            for ele in node.children:
                cur += deep(ele)
            cur += ']'
            return cur

        res = deep(root)
        print(res)
        return res

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if data == '':
            return None
        stack = []
        for c in data:
            if c == '[':
                if stack and type(stack[-1]) == str:
                    num = ''
                    while stack[-1] != '[':
                        num = stack.pop() + num
                    stack.append(Node(int(num), []))
                stack.append(c)
            elif c.isdigit():
                stack.append(c)
            else:
                if type(stack[-1]) == str:
                    num = ''
                    while stack[-1] != '[':
                        num = stack.pop() + num
                    stack.pop()
                    stack.append(Node(int(num), []))
                else:
                    cur = []
                    while stack[-1] != '[':
                        cur.append(stack.pop())
                    child = cur[:-1]
                    child.reverse()
                    cur[-1].children = child
                    # for i in range(len(cur)-1, -1, -1):
                    #     cur[-1].children.append(cur[i])
                    stack.pop()
                    stack.append(cur[-1])

        # print(stack[0].children[2].children[0])
        return stack[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))