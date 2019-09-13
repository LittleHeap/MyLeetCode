class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w = len(word)
        m = len(board)
        n = len(board[0])

        res = set()

        def deep(t, i, j, index):
            if True in res:
                return
            if index == w:
                res.add(True)
                return
            if index == 0:
                for a in range(m):
                    for b in range(n):
                        if t[a][b] == word[index]:
                            t[a][b] = 1
                            deep(t, a, b, index + 1)
                            t[a][b] = word[index]
            else:
                if i + 1 < m and t[i + 1][j] == word[index]:
                    t[i + 1][j] = 1
                    deep(t, i + 1, j, index + 1)
                    t[i + 1][j] = word[index]
                if i - 1 >= 0 and t[i - 1][j] == word[index]:
                    t[i - 1][j] = 1
                    deep(t, i - 1, j, index + 1)
                    t[i - 1][j] = word[index]
                if j + 1 < n and t[i][j + 1] == word[index]:
                    t[i][j + 1] = 1
                    deep(t, i, j + 1, index + 1)
                    t[i][j + 1] = word[index]
                if j - 1 >= 0 and t[i][j - 1] == word[index]:
                    t[i][j - 1] = 1
                    deep(t, i, j - 1, index + 1)
                    t[i][j - 1] = word[index]
                return

        deep(board, 0, 0, 0)

        return True in res
