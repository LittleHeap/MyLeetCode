class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        fang = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                curfang = (i // 3) * 3 + j // 3
                if board[i][j] not in row[i]:
                    row[i].add(board[i][j])
                else:
                    return False
                if board[i][j] not in col[j]:
                    col[j].add(board[i][j])
                else:
                    return False
                if board[i][j] not in fang[curfang]:
                    fang[curfang].add(board[i][j])
                else:
                    return False

        return True