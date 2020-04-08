class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]

        cur = [1]
        for _ in range(rowIndex):
            newcur = [1]
            for j in range(len(cur) - 1):
                newcur.append(cur[j] + cur[j + 1])
            newcur.append(1)
            cur = newcur

        return cur