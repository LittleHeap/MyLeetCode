class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.t = [[0 for _ in range(n)] for _ in range(n)]

        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.t[row][col] = player

        m = 1
        # left
        for j in range(col - 1, -1, -1):
            if self.t[row][j] == player:
                m += 1
            else:
                break
        # right
        for j in range(col + 1, self.n):
            if self.t[row][j] == player:
                m += 1
            else:
                break

        if m == self.n:
            return player
        else:
            m = 1

        # up
        for i in range(row - 1, -1, -1):
            if self.t[i][col] == player:
                m += 1
            else:
                break
        # down
        for i in range(row + 1, self.n):
            if self.t[i][col] == player:
                m += 1
            else:
                break

        if m == self.n:
            return player
        else:
            m = 1

        # left up
        i = row
        j = col
        while i - 1 >= 0 and j - 1 >= 0 and self.t[i - 1][j - 1] == player:
            m += 1
            i -= 1
            j -= 1

        i = row
        j = col
        while i + 1 < self.n and j + 1 < self.n and self.t[i + 1][j + 1] == player:
            m += 1
            i += 1
            j += 1

        if m == self.n:
            return player
        else:
            m = 1

        i = row
        j = col
        while i + 1 < self.n and j - 1 >= 0 and self.t[i + 1][j - 1] == player:
            m += 1
            i += 1
            j -= 1

        i = row
        j = col
        while i - 1 >= 0 and j + 1 < self.n and self.t[i - 1][j + 1] == player:
            m += 1
            i -= 1
            j += 1

        if m == self.n:
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)