board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
words = ["oath", "pea", "eat", "rain"]

m = len(board)
n = len(board[0])

res = set()


def deep(i, j, w, index):
    if index == len(w):
        res.add(w)
        return
    if (i - 1, j) not in hold and i - 1 >= 0 and board[i - 1][j] == w[index] and w not in res:
        if index == len(w) - 1:
            res.add(w)
            return
        hold.add((i - 1, j))
        deep(i - 1, j, w, index + 1)
        hold.remove((i - 1, j))
    if (i + 1, j) not in hold and i + 1 < m and board[i + 1][j] == w[index] and w not in res:
        if index == len(w) - 1:
            res.add(w)
            return
        hold.add((i + 1, j))
        deep(i + 1, j, w, index + 1)
        hold.remove((i + 1, j))
    if (i, j + 1) not in hold and j + 1 < n and board[i][j + 1] == w[index] and w not in res:
        if index == len(w) - 1:
            res.add(w)
            return
        hold.add((i, j + 1))
        deep(i, j + 1, w, index + 1)
        hold.remove((i, j + 1))
    if (i, j - 1) not in hold and j - 1 >= 0 and board[i][j - 1] == w[index] and w not in res:
        if index == len(w) - 1:
            res.add(w)
            return
        hold.add((i, j - 1))
        deep(i, j - 1, w, index + 1)
        hold.remove((i, j - 1))


for ele in words:
    for i in range(m):
        for j in range(n):
            if board[i][j] == ele[0]:
                hold = set()
                hold.add((i, j))
                deep(i, j, ele, 1)

print(res)
