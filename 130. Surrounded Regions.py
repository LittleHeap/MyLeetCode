board = [["X", "O", "O", "O", "X", "O", "O"],
         ["O", "X", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "X", "O", "O", "O"],
         ["X", "O", "O", "X", "X", "O", "X"],
         ["O", "X", "O", "O", "O", "O", "X"],
         ["O", "O", "O", "X", "O", "O", "O"]]

m = len(board)
n = len(board[0])
deal = set()
no = set()
d = {}


def deep(board, head, a, b):
    print(d)
    if a == None and b == None:
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in deal:
                    d[(i, j)] = [(i, j)]
                    deal.add((i, j))
                    if i + 1 == m or i == 0 or j + 1 == n or j == 0:
                        no.add((i, j))
                    deep(board, (i, j), i, j)
    else:
        if a == 0 or a == m - 1 or b == 0 or b == n - 1:
            no.add(head)
        if a - 1 >= 0 and board[a - 1][b] == 'O' and (a - 1, b) not in d[head]:
            deal.add((a - 1, b))
            d[head].append((a - 1, b))
            deep(board, head, a - 1, b)
        if a + 1 < m and board[a + 1][b] == 'O' and (a + 1, b) not in d[head]:
            deal.add((a + 1, b))
            d[head].append((a + 1, b))
            deep(board, head, a + 1, b)
        if b - 1 >= 0 and board[a][b - 1] == 'O' and (a, b - 1) not in d[head]:
            deal.add((a, b - 1))
            d[head].append((a, b - 1))
            deep(board, head, a, b - 1)
        if b + 1 < n and board[a][b + 1] == 'O' and (a, b + 1) not in d[head]:
            deal.add((a, b + 1))
            d[head].append((a, b + 1))
            deep(board, head, a, b + 1)
        return


deep(board, None, None, None)
for ele in d:
    if ele not in no:
        for index in d[ele]:
            board[index[0]][index[1]] = 'X'

print(board)

print(d)
print(no)
