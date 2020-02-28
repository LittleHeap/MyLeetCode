class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0

        if not board:
            return count

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == 'X':
                    if row > 0 and board[row - 1][column] == 'X':
                        continue
                    if column > 0 and board[row][column - 1] == 'X':
                        continue

                    count += 1

        return count