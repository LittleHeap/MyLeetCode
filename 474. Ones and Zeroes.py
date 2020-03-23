class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        hold = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for s in strs:
            z, o = s.count('0'), s.count('1')
            for i in range(n, -1, -1):
                for j in range(m, -1, -1):
                    if j >= z and i >= o:
                        hold[i][j] = max(hold[i][j], hold[i - o][j - z] + 1)

        return hold[-1][-1]