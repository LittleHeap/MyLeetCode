matrix = [[1, 2, 2, 3, 5],
          [3, 2, 3, 4, 4],
          [2, 4, 5, 3, 1],
          [6, 7, 1, 4, 5],
          [5, 1, 1, 2, 4]]

m = len(matrix)
n = len(matrix[0])

lr = []
done = set()
t = [[0 for _ in range(n)] for _ in range(m)]


def dfs(i, j, src, res):
    done.add((i, j))
    if i + 1 == m or j + 1 == n:
        for ele in src:
            t[ele[0]][ele[1]] = 1
        res.extend(src)
    else:
        if i + 1 < m and (i + 1, j) not in done:
            if matrix[i + 1][j] > matrix[src[0][0]][src[0][1]]:
                src = [(i + 1, j)]
            elif matrix[i + 1][j] == matrix[src[0][0]][src[0][1]] and (i, j) in src:
                src.append((i + 1, j))
            dfs(i + 1, j, src, res)
        if i - 1 >= 0 and (i - 1, j) not in done:
            if matrix[i - 1][j] > matrix[src[0][0]][src[0][1]]:
                src = [(i - 1, j)]
            elif matrix[i - 1][j] == matrix[src[0][0]][src[0][1]] and (i, j) in src:
                src.append((i - 1, j))
            dfs(i - 1, j, src, res)
        if j + 1 < n and (i, j + 1) not in done:
            if matrix[i][j + 1] > matrix[src[0][0]][src[0][1]]:
                src = [(i, j + 1)]
            elif matrix[i][j + 1] == matrix[src[0][0]][src[0][1]] and (i, j) in src:
                src.append((i, j + 1))
            dfs(i, j + 1, src, res)
        if j - 1 >= 0 and (i, j - 1) not in done:
            if matrix[i][j - 1] > matrix[src[0][0]][src[0][1]]:
                src = [(i, j - 1)]
            elif matrix[i][j - 1] == matrix[src[0][0]][src[0][1]] and (i, j) in src:
                src.append((i, j - 1))
            dfs(i, j - 1, src, res)


dfs(0, 0, [(0, 0)], lr)
print(lr)
