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

for i in range(9):
    for j in range(9):
        r = i
        c = j
        b = (i // 3) * 3 + j // 3
        if board[i][j] != '.':
            row[r].add(board[i][j])
            col[c].add(board[i][j])
            block[b].add(board[i][j])

ans = set()


def deep(i, j, row, col, block, m):
    print(m)
    if True in ans:
        return
    if i == '8' and j == '8':
        ans.add(True)
        return
    flag = 0
    for a in range(i, 9):
        for b in range(9):
            if m[a][b] != '.':
                continue
            else:
                flag = 1
                break
        if flag:
            break
    if a == 8 and b == 8 and m[a][b] != '.':
        ans.add(True)
        return
    r = a
    c = b
    o = (a // 3) * 3 + b // 3
    for test in range(1, 10):
        if str(test) in row[r] or str(test) in col[c] or str(test) in block[o]:
            continue
        else:
            print(test)
            newm = copy.deepcopy(m)
            newrow = copy.deepcopy(row)
            newcol = copy.deepcopy(col)
            newblock = copy.deepcopy(block)
            newm[a][b] = str(test)
            newrow[r].add(str(test))
            newcol[c].add(str(test))
            newblock[o].add(str(test))

            deep(a, b, newrow, newcol, newblock, newm)
    return


deep(0, 0, row, col, block, board)
print(ans)
