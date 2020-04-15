class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.mid = None
        self.right = None
        self.start = set()
        self.end = set()


class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node('a')

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """

        def deep(node, index):
            if index == len(word) - 1:
                if not node:
                    return Node(word[index])
                else:
                    node.end.add(len(word))
                    return
            if word[index] < node.val:
                if not node.left:
                    node.left = Node(word[index])
                deep(node.left, index + 1)
            elif word[index] == node.val:
                if not node.mid:
                    node.mid = Node(word[index + 1])
                deep(node.mid, index + 1)
            else:
                if not node.right:
                    node.right = Node(word[index])
                deep(node.right, index + 1)
        deep(self.head, 0)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def deep(node, index):
            if not node:
                return False
            if index == len(word) - 1:
                if node.val == word[index] and len(word) in node.end:
                    return True
                else:
                    return False
            if word[index] == '.':
                return deep(node.left, index + 1) or deep(node.mid, index + 1) or deep(node.right, index + 1)
            elif node.val == word[index]:
                if word[index] < node.val:
                    return deep(node.left, index + 1)
                elif word[index] == node.val:
                    return deep(node.mid, index + 1)
                else:
                    return deep(node.right, index + 1)
            else:
                return False

        q = [self.head]
        while q:
            newq = []
            ele = q.pop(0)
            if ele.val == word[0] or word[0] == '.':
                if deep(ele, 0):
                    return True
            else:
                if ele.left:
                    q.append(ele.left)
                if ele.mid:
                    q.append(ele.mid)
                if ele.right:
                    q.append(ele.right)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('bad')
print(obj.head.right.left.right.val)
# param_2 = obj.search(word)