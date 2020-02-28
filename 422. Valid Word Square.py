class Solution:
    def validWordSquare(self, words: List[str]) -> bool:

        m = len(words)

        matrix = [[] for _ in range(m)]

        for i in range(m):
            if len(words[i]) > m:
                return 0
            for j in range(len(words[i])):
                matrix[i].append(words[i][j])
            for _ in range(m - len(words[i])):
                matrix[i].append('0')

        for i in range(m):
            for j in range(i, m):
                if matrix[i][j] != matrix[j][i]:
                    return 0

        return 1
