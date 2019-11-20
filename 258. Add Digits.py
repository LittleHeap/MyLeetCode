class Solution:
    def addDigits(self, num: int) -> int:

        while len(str(num)) > 1:
            new = 0
            for n in str(num):
                new += int(n)
            num = new
        return num