import copy
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

row = [set() for _ in range(9)]
col = [set() for _ in range(9)]
fang = [set() for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j] != '.':
            row[i].add(int(board[i][j]))
            col[j].add(int(board[i][j]))
            fang[(i // 3) * 3 + j // 3].add(int(board[i][j]))

find = set()


def deep(loc, row, col, fang):
    if 1 in find:
        return
    if loc == 81:
        find.add(1)
        return
    i = loc // 9
    j = loc - i * 9
    f = (i // 3) * 3 + j // 3
    if board[i][j] != '.':
        while board[loc // 9][loc - (loc // 9) * 9] != '.':
            loc += 1
            if loc == 81:
                find.add(1)
                return
        deep(loc, row, col, fang)
    else:
        currow = copy.deepcopy(row)
        curcol = copy.deepcopy(col)
        curfang = copy.deepcopy(fang)
        hold = []
        for h in range(1, 10):
            if h not in currow[i] and h not in curcol[j] and h not in curfang[f]:
                hold.append(h)
        for h in hold:
            board[i][j] = str(h)
            currow[i].add(h)
            curcol[j].add(h)
            curfang[f].add(h)
            deep(loc + 1, currow, curcol, curfang)
            if 1 in find:
                return
            board[i][j] = '.'
            currow[i].remove(h)
            curcol[j].remove(h)
            curfang[f].remove(h)


deep(0, row, col, fang)
