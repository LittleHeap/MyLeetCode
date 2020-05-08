class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:

        m = len(nums)
        n = len(nums[0])

        if m * n != r * c:
            return nums

        res = [[0 for _ in range(c)] for _ in range(r)]
        x, y = 0, 0

        for i in range(m):
            for j in range(n):
                res[x][y] = nums[i][j]
                y += 1
                if y == c:
                    x += 1
                    y = 0

        return res