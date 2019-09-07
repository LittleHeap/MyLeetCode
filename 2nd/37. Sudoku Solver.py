import copy

board = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]

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

res = []


def deep(i, j, row, col, block, m):
    print(m)
    if True in ans:
        return
    if i == '8' and j == '8':
        ans.add(True)
        res.append(m)
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
        res.append(m)
        return
    r = a
    c = b
    o = (a // 3) * 3 + b // 3
    for test in range(1, 10):
        if str(test) in row[r] or str(test) in col[c] or str(test) in block[o]:
            continue
        else:
            m[a][b] = str(test)
            row[r].add(str(test))
            col[c].add(str(test))
            block[o].add(str(test))

            deep(a, b, row, col, block, m)
            if True in ans:
                return
            else:
                m[a][b] = '.'
                row[r].remove(str(test))
                col[c].remove(str(test))
                block[o].remove(str(test))
    return


deep(0, 0, row, col, block, board)

print(board)
