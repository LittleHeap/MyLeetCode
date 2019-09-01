board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]

word = "AAB"

res = set()


def deep(cur, i, j, index):
    if True in res:
        return
    if index == len(word):
        res.add(True)
        return
    if index == 0:
        for a in range(len(cur)):
            for b in range(len(cur[0])):
                if cur[a][b] == word[index]:
                    cur[a][b] = ''
                    deep(cur, a, b, index + 1)
                    cur[a][b] = word[index]
    else:
        if i - 1 >= 0 and cur[i - 1][j] == word[index]:
            cur[i - 1][j] = ''
            deep(cur, i - 1, j, index + 1)
            cur[i - 1][j] = word[index]
        if i + 1 < len(cur) and cur[i + 1][j] == word[index]:
            cur[i + 1][j] = ''
            deep(cur, i + 1, j, index + 1)
            cur[i + 1][j] = word[index]
        if j - 1 >= 0 and cur[i][j - 1] == word[index]:
            cur[i][j - 1] = ''
            deep(cur, i, j - 1, index + 1)
            cur[i][j - 1] = word[index]
        if j + 1 < len(cur[0]) and cur[i][j + 1] == word[index]:
            cur[i][j + 1] = ''
            deep(cur, i, j + 1, index + 1)
            cur[i][j + 1] = word[index]
        return


deep(board.copy(), 0, 0, 0)
if True in res:
    print(True)
else:
    print(False)
