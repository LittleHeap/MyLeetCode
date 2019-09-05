image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2

m = len(image)
n = len(image[0])
t = image[sr][sc]

def deep(i, j):
    image[i][j] = newColor
    if i - 1 >= 0 and image[i - 1][j] == t:
        deep(i - 1, j)
    if i + 1 < m and image[i + 1][j] == t:
        deep(i + 1, j)
    if j - 1 >= 0 and image[i][j - 1] == t:
        deep(i, j - 1)
    if j + 1 < n and image[i][j + 1] == t:
        deep(i, j + 1)
    return


deep(sr, sc)

print(image)
