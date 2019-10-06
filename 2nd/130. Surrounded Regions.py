board = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]

m = len(board)
n = len(board[0])
bad = set()
cur = set()
temp = set()


def deep(x, y):
    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
        temp.add(1)
    cur.add((x, y))
    if x - 1 >= 0 and board[x - 1][y] == 'O' and (x - 1, y) not in cur:
        if x - 1 == 0:
            temp.add(1)
        deep(x - 1, y)
    if x + 1 < m and board[x + 1][y] == 'O' and (x + 1, y) not in cur:
        if x + 1 == m - 1:
            temp.add(1)
        deep(x + 1, y)
    if y - 1 >= 0 and board[x][y - 1] == 'O' and (x, y - 1) not in cur:
        if y - 1 == 0:
            temp.add(1)
        deep(x, y - 1)
    if y + 1 < n and board[x][y + 1] == 'O' and (x, y + 1) not in cur:
        if y + 1 == n - 1:
            temp.add(1)
        deep(x, y + 1)


for i in range(m):
    for j in range(n):
        if board[i][j] == 'O' and (i, j) not in bad:
            cur = set()
            temp = set()
            deep(i, j)
            if 1 in temp:
                bad = bad | cur
            else:
                for index in cur:
                    print(index)
                    board[index[0]][index[1]] = 'X'

print(board)
