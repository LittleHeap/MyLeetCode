class Solution:
    def countArrangement(self, N: int) -> int:

        res = [0]

        def dfs(cur, index):
            if index == N + 1:
                res[0] += 1
                return
            for i, num in enumerate(cur):
                if num % index == 0 or index % num == 0:
                    dfs(cur[:i] + cur[i + 1:], index + 1)

        dfs([i for i in range(1, N + 1)], 1)

        return res[0]