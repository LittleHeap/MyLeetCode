class Solution:
    def longestLine(self, M: List[List[int]]) -> int:

        m = len(M)
        if not m:
            return 0
        n = len(M[0])
        if not n:
            return 0

        row = [None for _ in range(m)]
        r = 0
        col = [None for _ in range(n)]
        c = 0
        pie = [None for _ in range(m + n - 1)]
        p = 0
        na = [None for _ in range(m + n - 1)]
        t = 0

        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    if row[i] is None:
                        row[i] = [j, 1]
                        r = max(r, 1)
                    else:
                        if row[i][0] + 1 == j:
                            row[i][0] += 1
                            row[i][1] += 1
                            r = max(r, row[i][1])
                        else:
                            row[i][0] = j
                            row[i][1] = 1
                    if col[j] is None:
                        col[j] = [i, 1]
                        c = max(c, 1)
                    else:
                        if col[j][0] + 1 == i:
                            col[j][0] += 1
                            col[j][1] += 1
                            c = max(c, col[j][1])
                        else:
                            col[j][0] = i
                            col[j][1] = 1
                    if pie[i + j] is None:
                        pie[i + j] = [[i, j], 1]
                        p = max(p, 1)
                    else:
                        if pie[i + j][0][0] == i - 1 and pie[i + j][0][1] == j + 1:
                            pie[i + j][0] = [i, j]
                            pie[i + j][1] += 1
                            p = max(p, pie[i + j][1])
                        else:
                            pie[i + j] = [[i, j], 1]
                    if na[i - j + n - 1] is None:
                        na[i - j + n - 1] = [[i, j], 1]
                        t = max(t, 1)
                    else:
                        if na[i - j + n - 1][0][0] == i - 1 and na[i - j + n - 1][0][1] == j - 1:
                            na[i - j + n - 1][0] = [i, j]
                            na[i - j + n - 1][1] += 1
                            t = max(t, na[i - j + n - 1][1])
                        else:
                            na[i - j + n - 1] = [[i, j], 1]

        # print(row)
        # print(col)
        # print(pie)
        # print(na)
        return max(r, c, p, t)















