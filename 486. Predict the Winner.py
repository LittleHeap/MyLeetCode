class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        n = len(nums)

        save = {}

        def deep(i, j):
            if i == j:
                return nums[i]
            else:
                if (i, j) in save:
                    return save[(i, j)]
                left = nums[i] - deep(i + 1, j)
                right = nums[j] - deep(i, j - 1)
                save[(i, j)] = max(left, right)
                return max(left, right)

        return deep(0, n - 1) >= 0