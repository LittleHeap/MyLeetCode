class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        if n == 0:
            return 1

        a = [10, 81]
        j = 8
        for i in range(n - 2):
            a.append(a[-1] * j)
            j -= 1

        return sum(a[:n])