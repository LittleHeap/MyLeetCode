class Solution:
    def fib(self, n: int) -> int:

        if n <= 1:
            return n

        hold = [0 for _ in range(n + 1)]

        hold[1] = 1

        for i in range(2, n + 1):
            hold[i] = hold[i - 1] + hold[i - 2]

        return hold[n]