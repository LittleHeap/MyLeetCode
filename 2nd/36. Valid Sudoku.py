import copy

board = [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
         ["2", ".", ".", ".", ".", ".", ".", ".", "."],
         ["3", ".", ".", ".", ".", ".", ".", ".", "."],
         ["4", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", ".", "."],
         ["6", ".", ".", ".", ".", ".", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         ["8", ".", ".", ".", ".", ".", ".", ".", "."],
         ["9", ".", ".", ".", ".", ".", ".", ".", "."]]

row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
block = [set() for _ in range(9)]

ans = set()
for i in range(9):
    for j in range(9):
        r = i
        c = j
        b = (i // 3) * 3 + j // 3
        if board[i][j] != '.':
            if board[i][j] in row[r] or board[i][j] in col[c] or board[i][j] in block[b]:
                ans.add(False)
            else:
                row[r].add(board[i][j])
                col[c].add(board[i][j])
                block[b].add(board[i][j])

print(ans)

