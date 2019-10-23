class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        last = [1, 1]
        for i in range(2, rowIndex + 1):
            new = [1]
            for j in range(1, len(last)):
                new.append(last[j] + last[j - 1])
            new.append(1)
            last = new

        return last
