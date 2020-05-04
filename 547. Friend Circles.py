class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        n = len(M)
        hold = [i for i in range(n)]

        def find(index):
            if hold[index] == index:
                return index
            else:
                hold[index] = find(hold[index])
                return hold[index]

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    hold[find(i)] = find(j)

        for i in range(n):
            hold[i] = find(i)

        return len(set(hold))
