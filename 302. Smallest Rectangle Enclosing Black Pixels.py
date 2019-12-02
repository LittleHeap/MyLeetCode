class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m = len(image)
        n = len(image[0])
        done = set()


        def DFS(x, y):
            if (x, y) in done:
                return
            else:
                done.add((x, y))
                if x - 1 >= 0:
                    if image[x - 1][y] == '1':
                        DFS(x - 1, y)
                if x + 1 < m:
                    if image[x + 1][y] == '1':
                        DFS(x + 1, y)
                if y - 1 >= 0:
                    if image[x][y - 1] == '1':
                        DFS(x, y - 1)
                if y + 1 < n:
                    if image[x][y + 1] == '1':
                        DFS(x, y + 1)


        DFS(x, y)

        x_l = float('inf')
        x_r = float('-inf')
        y_u = float('-inf')
        y_d = float('inf')

        for ele in done:
            x = ele[0]
            y = ele[1]
            x_l = min(x_l, x)
            x_r = max(x_r, x)
            y_u = max(y_u, y)
            y_d = min(y_d, y)

        return ((x_r - x_l + 1) * (y_u - y_d + 1))