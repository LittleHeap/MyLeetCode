class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        if N % 14 == 0:
            N = 14
        else:
            N = N % 14

        cur = cells

        for _ in range(N):
            newcur = []
            for i in range(len(cur)):
                if i == 0 or i == len(cur) - 1:
                    newcur.append(0)
                else:
                    if (cur[i - 1] == 1 and cur[i + 1] == 1) or (cur[i - 1] == 0 and cur[i + 1] == 0):
                        newcur.append(1)
                    else:
                        newcur.append(0)
            cur = newcur

        return cur