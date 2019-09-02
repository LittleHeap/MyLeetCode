grid = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def construct(grid):
    n = len(grid)
    if n == 1:
        node = Node(grid[0][0], True, None, None, None, None)
        return node
    d = int(n / 2)
    tl, tr, bl, br = [], [], [], []
    for i, row in enumerate(grid):
        if i < d:
            tl.append(row[:d])
            tr.append(row[d:])
        else:
            bl.append(row[:d])
            br.append(row[d:])
    n1 = construct(tl)
    n2 = construct(tr)
    n3 = construct(bl)
    n4 = construct(br)
    if n1.val == n2.val and n2.val == n3.val and n3.val == n4.val and n1.val in [True, False]:
        node = Node(n1.val, True, None, None, None, None)
    else:
        node = Node('*', False, n1, n2, n3, n4)
    return node


node = construct(grid)
print(node.val)
print(node.isLeaf)
print(node.topLeft.isLeaf)
print(node.topRight)
print(node.bottomLeft)
print(node.bottomRight)
