class Node:
    def __init__(self, val=0, d=None):
        self.val = val
        self.children = d
        self.end = 0


class Solution:
    def replaceWords(self, dict: List[str], s: str) -> str:

        root = Node('', {})

        for ele in dict:
            cur = root
            for i, char in enumerate(ele):
                if char not in cur.children:
                    cur.children[char] = Node(char, {})
                cur = cur.children[char]
                if i == len(ele) - 1:
                    cur.end = 1

        res = []
        for word in s.split(' '):
            cur = root
            now = ''
            for i, char in enumerate(word):
                if char in cur.children:
                    now += char
                    cur = cur.children[char]
                    if cur.end or i == len(word) - 1:
                        res.append(now)
                        break
                else:
                    res.append(word)
                    break

        return ' '.join(res)