class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:

        cur = ''
        step = 0

        for i in range(len(B) // len(A) + 3):
            if B in cur:
                return step
            else:
                cur += A
                step += 1

        return -1