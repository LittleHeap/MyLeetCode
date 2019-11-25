class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        d = []
        for i in range(m):
            for j in range(n):
                res = []
                if i - 1 >= 0:
                    res.append(board[i - 1][j])
                    if j - 1 >= 0:
                        res.append(board[i - 1][j - 1])
                    if j + 1 < n:
                        res.append(board[i - 1][j + 1])
                if i + 1 < m:
                    res.append(board[i + 1][j])
                    if j - 1 >= 0:
                        res.append(board[i + 1][j - 1])
                    if j + 1 < n:
                        res.append(board[i + 1][j + 1])
                if j - 1 >= 0:
                    res.append(board[i][j - 1])
                if j + 1 < n:
                    res.append(board[i][j + 1])
                if board[i][j] == 1:
                    if res.count(1) < 2:
                        d.append([i, j])
                    elif res.count(1) > 3:
                        d.append([i, j])
                else:
                    if res.count(1) == 3:
                        d.append([i, j])
        for ele in d:
            board[ele[0]][ele[1]] = 1 - board[ele[0]][ele[1]]



