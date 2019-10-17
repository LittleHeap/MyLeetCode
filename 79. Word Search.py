board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "ABCB"

word = list(word)
find = [0]

m = len(board)
n = len(board[0])


def deep(i, j, cur, remain, used):
    if find[0] == 1:
        return
    if not remain:
        find[0] = 1
    else:
        if i - 1 >= 0 and board[i - 1][j] == remain[0] and (i - 1, j) not in used:
            newcur = cur.copy()
            newremain = remain.copy()
            newused = used.copy()
            newcur.append(board[i - 1][j])
            newremain.pop(0)
            newused.add((i - 1, j))
            deep(i - 1, j, newcur, newremain, newused)
        if i + 1 < m and board[i + 1][j] == remain[0] and (i + 1, j) not in used:
            newcur = cur.copy()
            newremain = remain.copy()
            newused = used.copy()
            newcur.append(board[i + 1][j])
            newremain.pop(0)
            newused.add((i + 1, j))
            deep(i + 1, j, newcur, newremain, newused)
        if j - 1 >= 0 and board[i][j - 1] == remain[0] and (i, j - 1) not in used:
            newcur = cur.copy()
            newremain = remain.copy()
            newused = used.copy()
            newcur.append(board[i][j - 1])
            newremain.pop(0)
            newused.add((i, j - 1))
            deep(i, j - 1, newcur, newremain, newused)
        if j + 1 < n and board[i][j + 1] == remain[0] and (i, j + 1) not in used:
            newcur = cur.copy()
            newremain = remain.copy()
            newused = used.copy()
            newcur.append(board[i][j + 1])
            newremain.pop(0)
            newused.add((i, j + 1))
            deep(i, j + 1, newcur, newremain, newused)


for i in range(m):
    if find[0] == 1:
        break
    for j in range(n):
        if find[0] == 1:
            break
        if board[i][j] == word[0]:
            cur = [board[i][j]]
            remain = word.copy()
            remain.pop(0)
            used = set()
            used.add((i, j))
            deep(i, j, cur, remain, used)

print(find[0])
