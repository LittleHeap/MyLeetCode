class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        m = len(image)
        if not m:
            return image
        n = len(image[0])
        if not n:
            return image

        done = set()

        def deep(i, j, origin):
            image[i][j] = newColor
            done.add((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if x < 0 or x >= m or y < 0 or y >= n or (x, y) in done or image[x][y] != origin:
                    continue
                else:
                    deep(x, y, origin)

        deep(sr, sc, image[sr][sc])

        return image