class Solution:
    def minSteps(self, n: int) -> int:

        if n == 1:
            return 0

        if n % 2 == 0:
            return self.minSteps(n // 2) + 2
        else:
            for i in range(3, n + 1, 2):
                if n % i == 0:
                    return self.minSteps(n // i) + i

