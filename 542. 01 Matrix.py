class Solution:
    def updateMatrix(self, A: List[List[int]]) -> List[List[int]]:

        m = len(A)
        if m == 0:
            return A
        n = len(A[0])
        if n == 0:
            return A

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    A[i][j] = float('inf')

        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    q = [(i, j)]
                    step = 0
                    while q:
                        newq = []
                        step += 1
                        for node in q:
                            x, y = node
                            for newx, newy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                                if newx >= 0 and newx < m and newy >= 0 and newy < n:
                                    if A[newx][newy] > step:
                                        A[newx][newy] = step
                                        newq.append((newx, newy))
                                    elif A[newx][newy] + 1 < A[x][y]:
                                        newq = []
                                        break

                        q = newq

        return A